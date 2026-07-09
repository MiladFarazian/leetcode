# 826. Most Profit Assigning Work
# https://leetcode.com/problems/most-profit-assigning-work/
# Difficulty: Medium | Language: python3 | Runtime: 261 ms | Memory: 19.7 MB

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        max_profit = 0
        i = 0
        max_profit_at_difficulty = 0

        for ability in worker:
            while i < len(jobs) and ability >= jobs[i][0]:
                max_profit_at_difficulty = max(max_profit_at_difficulty, jobs[i][1])
                i += 1
            max_profit += max_profit_at_difficulty
        
        return max_profit
