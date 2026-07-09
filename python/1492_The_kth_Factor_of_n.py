# 1492. The kth Factor of n
# https://leetcode.com/problems/the-kth-factor-of-n/
# Difficulty: Medium | Language: python3 | Runtime: 32 ms | Memory: 16.5 MB

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1,n+1):
            if n % i == 0:
                factors.append(i)
        if len(factors) < k:
            return -1
        else:
            return factors[k-1]
