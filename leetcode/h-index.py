# Given an array of integers citations where citations[i] is the number of
# citations a researcher received for their ith paper, return the
# researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as
# the maximum value of h such that the given researcher has published at least
# h papers that have each been cited at least h times.

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





class SolutionTests(TestCase):
    @classmethod
    def setUp(clss):
        mysol = Solution()
        clss.h_index = mysol.hIndex
        
    def test_case_1(self):
        self.assertEqual(self.h_index([3,0,6,1,5]), 3)

    def test_case2(self):
        self.assertEqual(self.h_index([100]), 1)

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
