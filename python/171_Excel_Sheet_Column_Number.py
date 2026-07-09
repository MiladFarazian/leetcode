# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/
# Difficulty: Easy | Language: python3 | Runtime: 0 ms | Memory: 17.8 MB

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        alphabet_dict = {
            "A": 1, "B": 2, "C": 3, "D": 4,
            "E": 5, "F": 6, "G": 7, "H": 8,
            "I": 9, "J": 10, "K": 11, "L": 12,
            "M": 13, "N": 14, "O": 15, "P": 16,
            "Q": 17, "R": 18, "S": 19, "T": 20,
            "U": 21, "V": 22, "W": 23, "X": 24,
            "Y": 25, "Z": 26
        }
        for i in range(len(columnTitle)):
            if i != 0:
                col_num = col_num * 26
            letter = columnTitle[i]
            col_num += alphabet_dict[letter]
        return col_num
