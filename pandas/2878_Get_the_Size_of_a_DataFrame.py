# 2878. Get the Size of a DataFrame
# https://leetcode.com/problems/get-the-size-of-a-dataframe/
# Difficulty: Easy | Language: pythondata | Runtime: 409 ms | Memory: 66 MB

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    size = [players.shape[0],players.shape[1]]
    return size
