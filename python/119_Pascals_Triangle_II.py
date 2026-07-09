# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/
# Difficulty: Easy | Language: python3 | Runtime: 0 ms | Memory: 17.5 MB

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = []
        row = [1]
        for i in range(rowIndex+1):
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
        return row
