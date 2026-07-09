# 2877. Create a DataFrame from List
# https://leetcode.com/problems/create-a-dataframe-from-list/
# Difficulty: Easy | Language: pythondata | Runtime: 340 ms | Memory: 65.6 MB

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    student_df = pd.DataFrame(student_data, columns=["student_id","age"])
    return student_df
