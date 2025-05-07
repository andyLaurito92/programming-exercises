"""
Check wether a string is a palindrome. A palindrome is a word
that can be read from left to right or right to left

Examples:
- rotator
- radar
- mom
"""

def ispalindrome(word: str) -> bool:
    i = 0
    j = len(word) - 1
    while i <= j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


assert True == ispalindrome("rotator")
assert False == ispalindrome("I'mnot")
assert True == ispalindrome("radar")
