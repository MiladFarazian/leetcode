# 67. Add Binary
# https://leetcode.com/problems/add-binary/
# Difficulty: Easy | Language: python3 | Runtime: 5 ms | Memory: 19.5 MB

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #start from right in a and b and move left, 
        #if both are "1", make rightmost element "0" and add 1 to next digit
        #if one is "0" and one is one "1", leave as 1
        #if both are "0", leave as zero
        i, j = len(a) - 1, len(b) - 1   # fingers on the rightmost digit of each
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))
