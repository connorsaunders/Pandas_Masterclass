'''
2878. Get the Size of a DataFrame
DataFrame players:
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+
Write a solution to calculate and display the number of rows and columns of players.

Return the result as an array:

[number of rows, number of columns]

The result format is in the following example.

 

Example 1:

Input:
+-----------+----------+-----+-------------+--------------------+
| player_id | name     | age | position    | team               |
+-----------+----------+-----+-------------+--------------------+
| 846       | Mason    | 21  | Forward     | RealMadrid         |
| 749       | Riley    | 30  | Winger      | Barcelona          |
| 155       | Bob      | 28  | Striker     | ManchesterUnited   |
| 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
| 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
| 883       | Ava      | 23  | Defender    | Chelsea            |
| 355       | Violet   | 18  | Striker     | Juventus           |
| 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
| 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
| 642       | Charlie  | 36  | Center-back | Arsenal            |
+-----------+----------+-----+-------------+--------------------+
'''


import pandas as pd
from typing import List


data = {
    "player_id": [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
    "name": ["Mason", "Riley", "Bob", "Isabella", "Zachary", "Ava", "Violet", "Thomas", "Jack", "Charlie"],
    "age": [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
    "position": ["Forward", "Winger", "Striker", "Goalkeeper", "Midfielder", "Defender", "Striker", "Striker", "Midfielder", "Center-back"],
    "team": ["RealMadrid", "Barcelona", "ManchesterUnited", "Liverpool", "BayernMunich", "Chelsea", "Juventus", "ParisSaint-Germain", "ManchesterCity", "Arsenal"]
}

df = pd.DataFrame(data)

print(df.columns)
print(df.shape)

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]


print(getDataframeSize(df))