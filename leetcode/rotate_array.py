"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

 

Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

 

Follow up:

    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

 
"""

from unittest import TestCase
import unittest
from io import StringIO

class Solution:
    def rotate1(self, nums:list[int], k: int) -> None:
        """
        This is the solution that takes O(N) in memory and O(N) in complexity
        """
        n = len(nums)
        k = k % n
        split = n - k
        new_array = []
        for i in range(split, n):
            new_array.append(nums[i])

        for i in range(0, split):
            new_array.append(nums[i])

        for i in range(n):
            nums[i] = new_array[i]


    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
        



class SolutionTests(TestCase):
    @classmethod
    def setUpClass(cls):
        mysolution = Solution()
        cls.rotate1 = mysolution.rotate1
        cls.rotate = mysolution.rotate

    def test_case1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3

        self.rotate1(nums, k)

        self.assertEqual([5, 6, 7, 1, 2, 3, 4], nums, "Rotate 1 didn't get expected result")

    def test_case2(self):
        nums = [-1, -2, 99, 100]
        k = 2

        self.rotate1(nums, k)

        self.assertEqual([99, 100, -1, -2], nums, "Rotate 1 didn't get expected result")

    def test_case3(self):
        nums = [1,2,3,4,5,6]
        k = 3

        self.rotate1(nums, k)

        self.assertEqual([4, 5, 6, 1, 2, 3], nums, "Rotate 1 didn't get expected result")

from pprint import pprint
stream = StringIO()
runner = unittest.TextTestRunner(stream=stream)
result = runner.run(unittest.makeSuite(SolutionTests))
print("tests run ", result.testsRun)
print("Errors ", result.errors)
pprint(result.failures)
stream.seek(0)
print("test output\n", stream.read())
