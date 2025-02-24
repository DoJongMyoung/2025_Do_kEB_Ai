import numpy as np

import pandas as pd

df = pd.DataFrame(
        [[4, 7, 10],
        [5, 8, 11],
        [6, 9, 12]] , index=[1, 2, 3],columns=['a', 'b', 'c']
)
#columns 설정 안하면 index 설정 안했을 때와 마찬가지로 0 1 2가 디폴트로 설정됨

print(df)

