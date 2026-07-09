# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy | Language: python3 | Runtime: 0 ms | Memory: 18.5 MB

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)
