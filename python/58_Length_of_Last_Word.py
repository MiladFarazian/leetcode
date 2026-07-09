# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy | Language: python3 | Runtime: 0 ms | Memory: 17.7 MB

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string_list = s.split()
        last_word = string_list[-1]
        return len(last_word)
