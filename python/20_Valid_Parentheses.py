# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy | Language: python3 | Runtime: 0 ms | Memory: 17.9 MB

class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(','{','['}
        match = {')':'(','}':'{',']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    open_bracket = stack.pop()
                    if open_bracket != match[s[i]]:
                        return False
        if not stack:
            return True
        else:
            return False
