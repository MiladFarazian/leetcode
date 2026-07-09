# 66. Plus One
# https://leetcode.com/problems/plus-one/
# Difficulty: Easy | Language: python3 | Runtime: 0 ms | Memory: 17.9 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)):
            print("i: " + str(i))
            print("len(digits): " + str(len(digits)))
            digits[-1-i] = digits[-1-i] + carry
            carry = 0
            if digits[-1-i] == 10:
                if i != len(digits)-1:
                    digits[-1-i] = 0
                    carry = 1
                else:
                    digits[-1-i] = 0
                    digits.insert(0, 1)
            print(digits[-1-i])
        return digits
