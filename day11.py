# Assignment
# v0.7) v0.6의 최근접이웃모델과 같이 동작하는 커스텀 클래스를 설계하시오.

from dolearn import KNeighborsRegressor
import pandas as pd
import matplotlib.pyplot as plt

ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")

model = KNeighborsRegressor()
result = model.sort(ls,31721.3)

print(model.predict(result))
print(model)

# KNeighborsRegressor 5.70