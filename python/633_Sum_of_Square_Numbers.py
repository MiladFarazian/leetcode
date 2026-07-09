# 633. Sum of Square Numbers
# https://leetcode.com/problems/sum-of-square-numbers/
# Difficulty: Medium | Language: python3 | Runtime: 95 ms | Memory: 16.6 MB

class Solution: 
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c)) + 1):
            b = c - a * a
            # Check if b is a perfect square
            if math.isqrt(b) ** 2 == b:
                return True
        return False
