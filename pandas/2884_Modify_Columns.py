# 2884. Modify Columns
# https://leetcode.com/problems/modify-columns/
# Difficulty: Easy | Language: pythondata | Runtime: 383 ms | Memory: 64.9 MB

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees
