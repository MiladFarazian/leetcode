# 2882. Drop Duplicate Rows
# https://leetcode.com/problems/drop-duplicate-rows/
# Difficulty: Easy | Language: pythondata | Runtime: 399 ms | Memory: 66.1 MB

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset="email")
