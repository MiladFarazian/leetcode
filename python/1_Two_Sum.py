# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Difficulty: Easy | Language: python | Runtime: 4464 ms | Memory: 14.5 MB

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    if nums[i] < nums[j]:
                        return [i,j]
                    else:
                        return [j,i]
