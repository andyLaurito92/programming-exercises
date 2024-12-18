# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        def swap(i, j, nums):
            nums[i], nums[j] = nums[j], nums[i]
        
        def find_next_distinct(i, current, nums):
            while i < len(nums) and current == nums[i]:
                i +=1
            if i >= len(nums):
                return False, i - 1
            else:
                return True, i

        i = 0
        idx_swap = 0
        while i < len(nums):
            current = nums[i]
            swap(idx_swap, i, nums)
            idx_swap += 1
            i = i + 1

            if i < len(nums) and nums[i] == current:
                swap(idx_swap, i, nums)
                idx_swap += 1
                # We already have 2 equal elements!
                # Let's find the sub-array in which we have 
                # all elements in [i + 1, j) being current
                found, j = find_next_distinct(i + 1, current, nums)
                if not found:
                    # This means we reached the end of the array and
                    # all elements were equal. We finished!
                    return idx_swap
                else:
                    # we know that from [i + 1, j) we have elements 
                    # that equal current. We need to start swapping 
                    # beginning in i + 1
                    i = j
        return idx_swap


        
