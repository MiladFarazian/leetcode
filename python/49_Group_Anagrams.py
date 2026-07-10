# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium | Language: python3 | Runtime: 9 ms | Memory: 22.3 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        keys = []
        for word in strs:
            key = ''.join(sorted(word))

            if key not in words:
                words[key] = []
                keys.append(key)
            words[key].append(word)
        
        out = []
        for i in range(len(words)):
            out.append(words[keys[i]])

        return out
