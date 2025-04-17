"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


from collections import defaultdict
from string import ascii_lowercase

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(list)
        for i, letter in enumerate(s):
            counter[letter].append(i)
            
        res = -1
        for letter, positions in counter.items():
            if len(positions) == 1 and (res == -1 or positions[0] < res):
                res = positions[0]
        return res

    def sol2(self, s:str) -> int:
        """
        Solution that uses ord for calculating
        index of ascii letters instead of mapping
        and float('inf')
        """
        counter = [0] * len(ascii_lowercase)
        first_pos = [-1] * len(ascii_lowercase)

        for i, c in enumerate(s):
            idx = ord(c) - ord('a') # Trick to convert ascii lowercase letter to [0,25] idx!!
            counter[idx] += 1
            if first_pos[idx] == -1:
                first_pos[idx] = i

        res = float('inf') # positive infinite! Useful for this case
        for i, count in enumerate(counter):
            if count == 1:
                res = min(res, first_pos[i])
        return res

        
        

sol = Solution()

assert 0 == sol.firstUniqChar('leetcode')
assert 0 == sol.sol2('leetcode')
