# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
# Difficulty: Easy | Language: python3 | Runtime: 0 ms | Memory: 17.7 MB

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            if i == 0:
                output.append([1])
            else:
                row = [1]
                prev = output[-1]
                for j in range(1,len(prev)):
                    new_added_val = prev[j-1] + prev[j]
                    row.append(new_added_val)
                row.append(1)
                output.append(row)
        return output
