# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Difficulty: Easy | Language: python3 | Runtime: 0 ms | Memory: 16.6 MB

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candyMax = max(candies)
        output = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= candyMax:
                output.append(True)
            else:
                output.append(False)
        return output
