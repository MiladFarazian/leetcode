# 2881. Create a New Column
# https://leetcode.com/problems/create-a-new-column/
# Difficulty: Easy | Language: pythondata | Runtime: 454 ms | Memory: 65.5 MB

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees
