# 2886. Change Data Type
# https://leetcode.com/problems/change-data-type/
# Difficulty: Easy | Language: pythondata | Runtime: 426 ms | Memory: 65.5 MB

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype('int')
    return students
