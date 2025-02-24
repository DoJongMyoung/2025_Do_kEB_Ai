import numpy as np

import pandas as pd

df = pd.DataFrame(
{  "a" : [4, 5, 6],
        "b" : [7, 8, 9],
        "c" : [10, 11, 12]},    )
#index는 행에 대한 index 역할을 함.
#딕셔너리의 키들은 열에 대한 이름 역할을 함.
print(df)

#index = [1, 2, 3]를 제거할 경우 0 1 2로 시작함.
