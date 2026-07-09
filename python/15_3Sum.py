# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Difficulty: Medium | Language: python | Runtime: 7231 ms | Memory: 16.7 MB

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        thr_sum = []
        nums.sort()
        for i in range(len(nums)-2):
            a = nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                if a + b + c == 0:
                    if [a, b, c] not in thr_sum:
                        thr_sum.append([a, b, c])
                    start += 1
                    end -= 1
                elif a + b + c > 0:
                    end -= 1
                else:
                    start += 1
        return thr_sum
