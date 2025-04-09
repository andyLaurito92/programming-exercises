"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef",
"cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not
a concatenated string because it is not the concatenation of any permutation of
words.

Return an array of the starting indices of all the concatenated substrings in s.
You can return the answer in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"]
which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"]
which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of
["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of
["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of
["the","foo","bar"].

Constraints:

    1 <= s.length <= 10^4
    1 <= words.length <= 5000
    1 <= words[i].length <= 30
    s and words[i] consist of lowercase English letters.
"""

from typing import List


"""
Let's use dynaimc programming

Subproblem space: prefixes? s[:i]
Relation between subproblems:
s(i) =
s(i-1) has current starting indices until s[:i-1]
Question: When we add s[i], do we have a new starting point?
What could have changed? It could have happened that when adding s[i],
some index from range(0, i) now becomes a concatenated string
But this only happens if s[i] is the last letter of that concatenated string!
and the above is true only if the start is s[i-m]. Why? Well, because if
this doesn't hold true, and the end was before s[i], then it should already
have been calculated in s(i-1), and we are stating that this is a new
starting point.

So s(i) = if isPermutation(s[i-m:i], words) then s(i-1).append(i-m) 

Topological order:  then for i in range(m, len(s))
Base case: len(s) < m => []
Original case: s(n)
Time

"""

from functools import reduce
from collections import defaultdict

class Solution:
    def ispermutation(self, s: str, words: dict[str, bool]) -> bool:
            """
            TODO: Study a better way to search for this concatenated
            string in s. Rabin-karp-algorithm?
            """
            if len(s) == 0 and all(words.values()):
                return True

            start = 0
            notused = {words: used for words, used in words.items() if not used}
            for word in notused:
                if hash(s[start:len(word)]) == hash(word):
                    words[word] = True
                    if self.ispermutation(s[len(word):], words):
                        return True
                    else:
                        words[word] = False
            return False

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m = reduce(lambda currsum, word: currsum + len(word), words, 0)
        if len(s) < m:
            return []

        n = len(s)
        # i represents the last string
        start = 0
        res = []
        for i in range(m, n):
            words_used = {word: False for word in words}
            if self.ispermutation(s[start:i], words_used):
                res.append(start)
            start += 1
            
        return res


sol = Solution()

assert True == sol.ispermutation("barfoo", {"foo":False, "bar":False})

assert [] == sol.findSubstring("something", ["something", "should", "be", "bigger"])
assert [0, 9] == sol.findSubstring("barfoothefoobarman", ["foo","bar"])
