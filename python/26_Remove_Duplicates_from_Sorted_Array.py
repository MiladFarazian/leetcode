# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy | Language: python3 | Runtime: 62 ms | Memory: 17.7 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        output = []
        for num in nums:
            if num not in seen:
                seen.add(num)
                output.append(num)
        nums[:] = output  # Modify the original list in-place
        return len(nums)
