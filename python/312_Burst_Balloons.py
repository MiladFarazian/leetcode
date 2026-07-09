# 312. Burst Balloons
# https://leetcode.com/problems/burst-balloons/
# Difficulty: Hard | Language: python | Runtime: 3177 ms | Memory: 13.6 MB

class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1, right):
                    coins = nums[left] * nums[i] * nums[right]
                    dp[left][right] = max(dp[left][right], dp[left][i] + coins + dp[i][right])

        # The answer is in dp[0][n-1] since it represents bursting all balloons (except the added ones)
        return dp[0][n - 1]
