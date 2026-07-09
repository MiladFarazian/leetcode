# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Difficulty: Medium | Language: python3 | Runtime: 1540 ms | Memory: 31.6 MB


import numpy as np
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k - 1):
            x = np.argmax(nums)
            nums.pop(x)
        return max(nums)
            
            
        #return sorted(nums)[len(nums) - k]
