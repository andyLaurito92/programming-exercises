# Given an array of integers citations where citations[i] is the number of
# citations a researcher received for their ith paper, return the
# researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as
# the maximum value of h such that the given researcher has published at least
# h papers that have each been cited at least h times.


# Constraints:

#     n == citations.length
#     1 <= n <= 5000
#     0 <= citations[i] <= 1000



"""
Important note: The length of the citations array is narrowed to 5000. This means that on
the worst case, the list will be of 5000 citations (it's maximum)

The proposed algorithm runs in O(N^2). Since N cannot be greater than 5000 => We know that the
algorithm will take ~ at most 5000^2 operations to finish => 25.000.000 (25 million operations)

Given that this array fits in memory, we know that according to this reference https://gist.github.com/hellerbarde/2843375
we take around 100ns to get a value from it => We will perform 25.000.000 which will take in the worst case 100ns =>
25.000.000 * 100 = 2.500.000.000 (2 billion, 500 million nanoseconds) = 2.5 seconds :)


The take away is: Because N is cap, the brute force approach is not that bad!

Can we do it better?
What is not performant of this solution is that is going several times on the
same part of the array and it doesn't reuse what it knows from previous runs
"""

from unittest import TestCase

class Solution:
    def _update_hidx(self, greatest_h_idx: int, found_h_idx: int) -> int:
        return found_h_idx if found_h_idx > greatest_h_idx else greatest_h_idx

    # [4, 3, 3]
    def hIndex(self, citations: list[int]) -> int:
        total_published_papers = len(citations)
        greatest_h_idx = 0
        for i in range(total_published_papers):
            num_citation_ith = citations[i]
            if num_citation_ith == 0:
                continue
            elif num_citation_ith == 1:
                # I have 1 paper (this one) that at least has 1 citation :)
                greatest_h_idx = self._update_hidx(greatest_h_idx, 1)
                continue
            h_idx = 1 # At least I have 1 paper with num_citation_ith
            for j in range(total_published_papers):
                if i == j:
                    # We don't count the same paper
                    continue
                # Let's see if we have num_citation_ith papers that have at least num_citation_ith
                if num_citation_ith <= citations[j]:
                    # Then paper j has at least num_citation_ith
                    h_idx +=1
                    if h_idx == num_citation_ith:
                        # We found num_citation_ith papers that have at least num_citation_ith!
                        break
            # We found num_citation_ith papers that have at least num_citations_ith
            greatest_h_idx = self._update_hidx(greatest_h_idx, h_idx)
        return greatest_h_idx

    def hIndex2(self, citations: list[int]) -> int:
        n = len(citations)

        citations.sort() # sort in a non-decreasing order
        greatest_h_idx = 0 
        for j in range(len(citations)):
            num_citations_jth = citations[j]
            if n - j >= num_citations_jth: # Because is non-decreasing, I have at least num_citations_jth publications with num_citations_jth citatinos
                greatest_h_idx = num_citations_jth
            else: 
                greatest_h_idx = max(n - j, greatest_h_idx)
                
        return greatest_h_idx


class SolutionTests(TestCase):
    @classmethod
    def setUp(clss):
        mysol = Solution()
        #clss.h_index = mysol.hIndex
        clss.h_index = mysol.hIndex2
        
    def test_case_1(self):
        self.assertEqual(self.h_index([3,0,6,1,5]), 3)

    def test_case2(self):
        self.assertEqual(self.h_index([100]), 1)

    def test_case3(self):
        self.assertEqual(self.h_index([1,3,1]), 1)

    def test_case4(self):
        self.assertEqual(self.h_index([0, 0, 2]), 1)

    def test_case5(self):
        self.assertEqual(self.h_index([11, 15]), 2)

    def test_case6(self):
        self.assertEqual(self.h_index([0, 0, 0, 4, 3, 2]), 2)

    def test_case7(self):
        self.assertEqual(self.h_index([4,4,0,0]), 2)


from pprint import pprint
from io import StringIO
stream = StringIO()
runner = unittest.TextTestRunner(stream=stream)
result = runner.run(unittest.makeSuite(SolutionTests))
print("tests run ", result.testsRun)
print("Errors ", result.errors)
pprint(result.failures)
stream.seek(0)
print("test output\n", stream.read())
