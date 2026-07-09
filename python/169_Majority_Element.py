# 169. Majority Element
# https://leetcode.com/problems/majority-element/
# Difficulty: Easy | Language: python3 | Runtime: 184 ms | Memory: 18.1 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        for i in range(len(nums)):
            num_dict[str(nums[i])] = 0
        for i in range(len(nums)):
            num_dict[str(nums[i])] += 1
        print(num_dict)
        inverse = [(value, key) for key, value in num_dict.items()]
        majority = max(inverse)[1]
        print(majority)
        return int(majority)
