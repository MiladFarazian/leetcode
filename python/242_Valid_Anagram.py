# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy | Language: python3 | Runtime: 15 ms | Memory: 19.5 MB

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1

        if s_dict == t_dict:
            return True
        else:
            return False
