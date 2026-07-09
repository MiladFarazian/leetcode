# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Difficulty: Easy | Language: python3 | Runtime: 2 ms | Memory: 16.7 MB

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        occurrences = []
        i = 0
        j = n = len(needle)
        while j <= len(haystack):
            print(haystack[i:j])
            if haystack[i:j] == needle:
                occurrences.append(i)
                print(i)
            i += 1
            j += 1
        if occurrences != []:
            return occurrences[0]
        else:
            return -1
