# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/
# Difficulty: Easy | Language: python3 | Runtime: 19 ms | Memory: 17.7 MB

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        for i in range(len(t)):
            if t[i] in s:
                s.remove(t[i])
            else:
                return t[i]
