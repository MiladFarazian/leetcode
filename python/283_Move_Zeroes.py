# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy | Language: python3 | Runtime: 3 ms | Memory: 18.8 MB

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
