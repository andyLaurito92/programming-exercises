"""
Given a string s, return the longest in s.

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

"""

def ispalindrome(mystring: str, start:int, end:int) -> bool:
    i = start
    j = end - 1
    while i <= j:
        if mystring[i] != mystring[j]:
            return False
        i += 1
        j -= 1
    return True


"""
Naive solution: We just iterate over the space of substrings
and we validate if our substring is both a palindrome and is
the longest one

Runtime: O(N^3) 
Space: O(1)
"""
def longestPalindrome1(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    res = None
    for i in range(n):
        for j in range(i, n+1):
            if ispalindrome(s, i, j):
                if res is None or j - i + 1 > res[1] - res[0] + 1:
                    res = (i, j)

    return s[res[0]:res[1]] if res else ''

"""
Let's be smarter: 1 thing for sure we can optimize: We don't need
to iterate from start to find out if sht is a palindrome, because
you move your iteratores just 1 pos at a time! Meaning that u know
the previous characters u had + the new one
"""

"""
Similar as above, but we change the way of how we iterate over
the string! Instead of iterating over indexes, we iterate over
lengths. 

Becuase we want the longest palindrome substring, then is as easy
as iterating over the lengths, starting with the longest length which is n,
and slowly decrease the length until we found a valid palindrome!
When iterating like this, once we found out a valid palindrome, then we can stop!
Why? Because we are iterating from the longest length to the shortest one, therefore,
the first palindrome that we find is gonna be the longest (there might be others of
the same length, but not of more length, otherwise, we should have found it in a
previous iteration)

Runtime: O(N^3)
Space: O(1)
"""

def longestPalindrome2(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s
    
    for length in reversed(range(1, n+1)):
        for i in range(0, n - length + 1):
            j = i + length
            if ispalindrome(s, i, j):
                return s[i:j]
    return ''

"""
In order to improve our above algorithm, we need to be smarter on the way we
calculate isPalindrome. Let's first start w/dyanmic programming and memoising
s[i:j]
"""
from collections import defaultdict

def longestPalindrome3(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    # we represent [start][length]. Because length = 0 doens't make sense
    # we need to create a n*(n+1) matrix
    memory = [[False] for _ in range(n+1)] * n

    for i in range(n):
        memory[i][1] = True # strings of length 1 are palindromes

    res = None
    # babad
    # xc0c1.cn/2-1cn/2cn/2-1...c1c0y
    for length in range(2, n):
        for i in range(0, n - length + 1):
            center = i + (i + length) // 2
            if memory[i][length - 1] and s[i-1] == s[length+1]:
                memory[i-1][length+1] = True


from typing import Optional


"""
Expanding around centers

Runtime: O(N^2)
Space: O(1)
"""
def longestPalindrome4(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    res = None
    def checkpalindrome(left: int, right: int):
        res = None
        while left >= 0 and right <= n - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        # left + 1 and right -1 was the last valid palindrome
        left += 1
        right -= 1
        if s[left] != s[right]:
            # no valid palindrome found
            return None

        if res is None or res[1] - res[0] + 1 < right - left + 1:
            res = (left, right)
        return res

    def update(new_pal: tuple[int, int], res: Optional[tuple[int, int]]):
        if new_pal is None:
            return res
        elif res is None:
            return new_pal
        elif new_pal[1] - new_pal[0] + 1 > res[1] - res[0] + 1:
            return new_pal
        else:
            return res

    for i in range(n - 1):
        new_pal = checkpalindrome(i, i)
        res = update(new_pal, res)

        new_pal = checkpalindrome(i, i+1)
        res = update(new_pal, res)

    return s[res[0]:res[1]+1] if res else s[0:1]


"""
TODO: There is a trick for solving this in O(N) but it's not trivial at all. Is more
for competitive programming. The algorithm is called Manacher's algorithm
"""


functions = [longestPalindrome1, longestPalindrome2, longestPalindrome4]
for fun in functions:
    assert "bab" == fun("babad")
    assert "bb" == fun("cbbd")
    assert "aabbdcecdbbaa" == fun("aabbdcecdbbaa")
    assert "n" == fun("nopalindrome")
