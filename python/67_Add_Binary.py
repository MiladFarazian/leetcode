# 67. Add Binary
# https://leetcode.com/problems/add-binary/
# Difficulty: Easy | Language: python3 | Runtime: 0 ms | Memory: 19.1 MB

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #start from right in a and b and move left, 
        #if both are "1", make rightmost element "0" and add 1 to next digit
        #if one is "0" and one is one "1", leave as 1
        #if both are "0", leave as zero

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            k = carry
            if i >= 0:
                k += int(a[i])
            if j >= 0:
                k += int(b[j])

            if k == 0:
                result.append("0")
                carry = 0
            elif k == 1:
                result.append("1")
                carry = 0
            elif k == 2:
                result.append("0")
                carry = 1
            else:
                result.append("1")
                carry = 1
        
            i = i - 1
            j = j - 1

        return "".join(reversed(result))
