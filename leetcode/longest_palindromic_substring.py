"""
Given a string s, return the longest in s.

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

"""

def ispalindrome(mystring: str) -> bool:
    i = 0
    j = len(mystring) - 1
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
            if ispalindrome(s[i:j]):
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
"""
def longestPalindrome2(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s
    
    for length in reversed(range(1, n+1)):
        for i in range(0, n - length + 1):
            j = i + length
            if ispalindrome(s[i:j]):
                return s[i:j]
    return ''


functions = [longestPalindrome1, longestPalindrome2]
for fun in functions:
    assert "bab" == fun("babad")
    assert "bb" == fun("cbbd")
    assert "aabbdcecdbbaa" == fun("aabbdcecdbbaa")
    assert "n" == fun("nopalindrome")
