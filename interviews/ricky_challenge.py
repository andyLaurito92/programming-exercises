"""
Given a list of words, find the word that has more anagrams in
the list

example: ["roma", "amor", "rosa", "paris", "ramo", "prisa", "mora"]
output: "roma"
"""

from collections import defaultdict

def most_anagrams(words: list[str]) -> str:
    """
    Given a list of words, find the word that has more anagrams in
    the list
    """
    def idxchar(achar: str) -> int:
        return ord(achar) - ord('a')

    if words is None:
        return None
    elif len(words) < 1:
        return None

    letters_per_word_frequency = defaultdict(int)
    res = words[0]
    curr_max = 0
    for word in words:
        letters = tuple(word)
        letters_per_word_frequency[letters] += 1
        if letters_per_word_frequency[letters] > curr_max:
            curr_max = letters_per_word_frequency[letters]
            res = word
    return res


assert "roma" == most_anagrams(["roma", "amor", "rosa", "paris", "ramo", "prisa", "mora"])

assert None is most_anagrams([])

assert None is most_anagrams(None)
