# 2879. Display the First Three Rows
# https://leetcode.com/problems/display-the-first-three-rows/
# Difficulty: Easy | Language: pythondata | Runtime: 412 ms | Memory: 65.6 MB

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
