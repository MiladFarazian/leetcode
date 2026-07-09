# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy | Language: python | Runtime: 103 ms | Memory: 13.5 MB

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        st = str(x)
        for i in range(len(st)/2):
            if st[i] != st[-i-1]:
                return False
        return True
