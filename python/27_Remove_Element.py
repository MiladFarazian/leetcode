# 27. Remove Element
# https://leetcode.com/problems/remove-element/
# Difficulty: Easy | Language: python | Runtime: 18 ms | Memory: 11.6 MB

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        while k < len(nums):
            if nums[k] == val:
                del nums[k]
            else:
                k = k + 1
        return k
