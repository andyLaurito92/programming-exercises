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
from collections import Counter

class Solution:
    def ispermutation(self, s: str, start: int, words: dict[str, int]) -> bool:
            """
            TODO: Study a better way to search for this concatenated
            string in s. Rabin-karp-algorithm?
            """
            unique_values = set(words.values())
            if len(unique_values) == 1 and 0 in unique_values:
                return True

            for word, count in words.items():
                if count != 0 and s.startswith(word, start):
                    words[word] -= 1
                    if self.ispermutation(s, start + len(word), words):
                        return True
                    else:
                        words[word] += 1
            return False

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m = reduce(lambda currsum, word: currsum + len(word), words, 0)
        concatstrlen = sum(map(len, words))

        if len(s) < m:
            return []

        n = len(s)
        # i represents the last string
        start = 0
        res = []
        words_used = Counter(words)
        for i in range(m, n+1): # Slices don't include last value!!
            if self.ispermutation(s, start, dict(words_used)):
                res.append(start)
            start += 1
            
        return res


sol = Solution()

assert True == sol.ispermutation("barfoo", 0, {"foo":1, "bar":1})

assert [] == sol.findSubstring("something", ["something", "should", "be", "bigger"])
assert [0, 9] == sol.findSubstring("barfoothefoobarman", ["foo","bar"])

assert [6, 9, 12] == sol.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])


assert [8] == sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])

"""
Lesson learned:

Creating a slice s[start:end] creates a new substring! Which means that it's complexity
equals the length of the slice. If we just want to compare characters, is way faster to
use method startwith(prefix, start, end)
"""


"""
To think about: Perhaps we can use Knuth - Morris - Prat algorithm and https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm to build an automaton that matches all words at the same time?
"""
