# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
# Difficulty: Easy | Language: python3 | Runtime: 24 ms | Memory: 14.3 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        n_binary = bin(n)[2:]
        total = 0
        for i in n_binary:
            if i == '1':
                total += 1
                
        return total
