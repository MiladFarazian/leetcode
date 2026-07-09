# 1404. Number of Steps to Reduce a Number in Binary Representation to One
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# Difficulty: Medium | Language: python | Runtime: 16 ms | Memory: 11.6 MB

class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        #two = 1
        for i in range(len(s)):
            j = len(s) - i - 1
            if s[j] == "1":
                num += 2**i
            #two = two * 2
        
        steps = 0
        while num != 1:
            if num % 2 == 1: #odd
                num += 1
            else:            #even
                num = num // 2
            steps += 1
        return steps
