# 2885. Rename Columns
# https://leetcode.com/problems/rename-columns/
# Difficulty: Easy | Language: pythondata | Runtime: 418 ms | Memory: 65.5 MB

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={'id':'student_id','first':'first_name','last':'last_name','age':'age_in_years'})
    return students
