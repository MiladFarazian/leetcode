# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Difficulty: Easy | Language: python3 | Runtime: 18 ms | Memory: 17.5 MB

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i','o','u','A','E','I','O','U',]
        reverse_vowel_str = list(s)
        i = 0
        j = len(s) - 1
        while i <= j:
            if reverse_vowel_str[i] in vowel and reverse_vowel_str[j] in vowel:
                reverse_vowel_str[i] = s[j]
                reverse_vowel_str[j] = s[i]
                i += 1
                j -= 1
            elif reverse_vowel_str[i] in vowel:
                j -= 1
            elif reverse_vowel_str[j] in vowel:
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(reverse_vowel_str)
