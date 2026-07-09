# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# Difficulty: Easy | Language: python3 | Runtime: 962 ms | Memory: 17.9 MB

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i * i <= x:
            i += 1
        return i - 1
