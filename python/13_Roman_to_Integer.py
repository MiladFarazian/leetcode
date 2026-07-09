# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy | Language: python3 | Runtime: 2 ms | Memory: 17.9 MB

class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
        }
        total = 0
        prev_value = 0  # value of the symbol to the right (in original string)

        for ch in reversed(s):
            curr = vals[ch]
            if curr < prev_value:
                total -= curr
            else:
                total += curr
            prev_value = curr

        return total
