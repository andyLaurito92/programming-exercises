from unittest import TestCase
import unittest
from io import StringIO


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True # I'm already in the last position!
        
        current = 0
        last_position = len(nums) - 1
        while current <= last_position:
            if nums[current] != 0:
                if current + nums[current] >= last_position:
                    return True
                # I can always jump 1 :)
                current += 1 
            else: 
                """ 
                Found a 0! Need to check how far I need to jump from my current position
                """
                idx_zeroes = current + 1
                while idx_zeroes <= last_position and nums[idx_zeroes] == 0:
                    idx_zeroes += 1 
                num_zeroes = idx_zeroes - current
                # Question: Do I have a jump that allows me jump further these zeroes?
                idx_jump_zeroes = current - 1
                need_to_jump = num_zeroes
                while idx_jump_zeroes > -1:
                    max_jump_length = nums[idx_jump_zeroes]
                    if idx_jump_zeroes + max_jump_length == last_position:
                        return True
                    elif max_jump_length > need_to_jump:
                        # I can jump these zeroes! and idx_jump_zeroes has the jump that allows me to do it.
                        # Keep going
                        break
                    idx_jump_zeroes -= 1 # Checking if a previous jump allows me to jump further
                    need_to_jump += 1 # The further I move from zeroes, the further I need to jump!
                
                if idx_jump_zeroes == -1:
                    return False
                else: # Keep checking from after zeroes
                    current += num_zeroes
        return False
                    


    def canJump2(self, nums: list[int]) -> bool:
        last_position = len(nums) - 1
        def canJumpToEndBacktracking(nums: list[int], fromidx:int) -> bool:
            if fromidx == last_position:
                return True
            elif fromidx > last_position:
                return False

            max_jump_length = nums[fromidx]
            if max_jump_length + fromidx == last_position:
                return True
            else:
                jump_length = 1
                while jump_length <= max_jump_length:
                    if canJumpToEndBacktracking(nums, fromidx + jump_length):
                        return True
                    jump_length += 1
            return False

        return canJumpToEndBacktracking(nums, 0)


class SolutionsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        mysolution = Solution()
        cls.canJump = mysolution.canJump

    def test_case1(self):
        self.assertTrue(self.canJump([1, 1, 2, 2, 0, 1, 1]))

    def test_case2(self):
        self.assertFalse(self.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))


stream = StringIO()
runner = unittest.TextTestRunner(stream=stream)
result = runner.run(unittest.makeSuite(SolutionsTests))
stream.seek(0)
print("test output\n", stream.read())
