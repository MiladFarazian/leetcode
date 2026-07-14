# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy | Language: python3 | Runtime: 16 ms | Memory: 37.2 MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                return True
        
        return False
