# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy | Language: python3 | Runtime: 30 ms | Memory: 16.5 MB

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergestr = ""
        i = 0
        n = len(word1)
        m = len(word2)
        while i < n and i < m:
            mergestr += word1[i]
            mergestr += word2[i]
            i += 1
        if i < n:
            mergestr += word1[i:n]
        elif i < m:
            mergestr += word2[i:m]
        return mergestr
