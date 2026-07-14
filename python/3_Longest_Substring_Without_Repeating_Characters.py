# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium | Language: python3 | Runtime: 8 ms | Memory: 19.4 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}   # notebook: letter -> where I last saw it
        left = 0
        best = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:# is this letter a problem for my current window?
                left = last_seen[char] + 1   # jump left past the old copy
            last_seen[char] = right   # update the notebook
            best = max(best, right - left + 1)   # how big is the window right now?

        return best
