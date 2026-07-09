# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium | Language: python3 | Runtime: 3 ms | Memory: 19.3 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}   # char -> index of its most recent occurrence
        left = 0
        best = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right
            best = max(best, right - left + 1)

        return best
