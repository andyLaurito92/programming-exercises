from operator import itemgetter
"""
You are given a string s and an integer k. You can choose any character of the
string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can
get after performing the above operations.

Constraints
    1 <= s.length <= 10^5
    s consists of only uppercase English letters.
    0 <= k <= s.length

"""

from collections import Counter

"""
First approach, naive.
Runtime: O(N^3)

Explanation: Just grab each possible substring, count the number of
characters you have in it and try to convert all characters != to
the most frequent character.

If your k is big enough to do so, then you found a valid substring.
We need to check if this is the longest one

Why this is naive?
- I'm not really ussing the uppercase constraint
- I'm recalculating in every step the counter, while we know that this
only changes in 1 character every time :)
"""

def characterReplacementNaive(s: str, k: int) -> int:
    n = len(s)
    if n < 2:
        return n

    res = 0
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            counter = Counter(substr)
            max_freq = max(counter.values())
            to_replace = len(substr) - max_freq
            if to_replace <= k:
                res = max(len(substr), res)
    return res


from string import ascii_uppercase

def characterReplacement2(s: str, k: int) -> int:
    n = len(s)
    r = len(ascii_uppercase)

    if n < 2:
        return n

    def idxchar(c:str) -> int:
        return ord(c) - ord('A')

    maxcharcount = [[0] * r for _ in range(n)]
    maxcharcount[0][idxchar(s[0])] += 1
    for i in range(1, n):
        for j in range(r):
            maxcharcount[i][j] = maxcharcount[i-1][j]
        maxcharcount[i][idxchar(s[i])] += 1


    def getcharcount(i: int, j:int) -> list[list[int]]:
        if i == 0:
            return maxcharcount[j]

        start = maxcharcount[i]
        end = maxcharcount[j]
        res = [0] * r

        for m in range(r):
            res[m] = end[m] - start[m]

        return res


    res = 0
    for i in range(n):
        for j in range(i, n):
            charcount = getcharcount(i, j)
            max_freq = 0
            for m in range(r):
                if charcount[m] > max_freq:
                    max_freq = charcount[m]

            len_substr = (j - i + 1)
            to_replace = len_substr - max_freq
            if to_replace <= k:
                res = max(len_substr, res)
    return res


for fun in [characterReplacementNaive, characterReplacement2]:
    assert 4 == fun("ABAB", 2), f"Failed w/fn {fun}, input: ABAB k = 2"
    assert 3 == fun("AAAB", 0)
    assert 4 == fun("AABABBA", 1)
    assert 4 == fun("ABBB", 2)
