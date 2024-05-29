# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/submissions/1271676308?envType=daily-question&envId=2024-05-29

# Number of Steps to Reduce a Number in Binary Representation to One
class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in range(len(s)):
            j = len(s) - i - 1
            if s[j] == "1":
                num += 2**i
        
        steps = 0
        while num != 1:
            if num % 2 == 1: #odd
                num += 1
            else:            #even
                num = num // 2
            steps += 1
        return steps