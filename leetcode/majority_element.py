# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# This can be solved in O(N) & O(1) space by using the
# the Boyer-moore majority vote algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        occurrences = {}
        for elem in nums:
            if not elem in occurrences:
                occurrences[elem] = 1
            else:
                occurrences[elem] = occurrences[elem] + 1
        
        return sorted(occurrences.items(), key=lambda x: x[1], reverse=True)[0][0]

    def boyer_moore_voting_algorithm(self, nums:list[int]) -> int:
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if num == candidate else -1

        return candidate
        

        
