# 945. Minimum Increment to Make Array Unique
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/
# Difficulty: Medium | Language: python3 | Runtime: 673 ms | Memory: 34.5 MB

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        
        moves = 0
        excess = 0
        
        for x in range(max(nums) + len(nums)):
            if count[x] > 1:
                excess += count[x] - 1
                moves -= x * (count[x] - 1)
            elif excess > 0 and count[x] == 0:
                excess -= 1
                moves += x
        
        return moves
