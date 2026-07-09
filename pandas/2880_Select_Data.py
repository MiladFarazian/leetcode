# 2880. Select Data
# https://leetcode.com/problems/select-data/
# Difficulty: Easy | Language: pythondata | Runtime: 400 ms | Memory: 65.7 MB

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    selected_students = students[students['student_id'] == 101].drop(columns=['student_id'])
    return selected_students
