# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/
# Difficulty: Easy | Language: python3 | Runtime: 0 ms | Memory: 18 MB

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col_letter = ""
        col_num = columnNumber
        reverse_alphabet_dict = {
            1: "A", 2: "B", 3: "C", 4: "D",
            5: "E", 6: "F", 7: "G", 8: "H",
            9: "I", 10: "J", 11: "K", 12: "L",
            13: "M", 14: "N", 15: "O", 16: "P",
            17: "Q", 18: "R", 19: "S", 20: "T",
            21: "U", 22: "V", 23: "W", 24: "X",
            25: "Y", 0: "Z"
        }
        while col_num > 0:
            num = col_num % 26
            letter = str(reverse_alphabet_dict[num])
            col_letter = letter + "" + col_letter
            print(col_letter)
            col_num = (col_num - 1) // 26
        return col_letter
