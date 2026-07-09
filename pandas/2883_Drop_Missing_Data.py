# 2883. Drop Missing Data
# https://leetcode.com/problems/drop-missing-data/
# Difficulty: Easy | Language: pythondata | Runtime: 458 ms | Memory: 66.4 MB

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.dropna(subset="name")
    return students
