# from statistics import LinearRegression
# from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import matplotlib.pyplot as plt

# 책에서는 2줄인거 한줄로 편하게함
ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")

# print(type(ls))
# print(ls)

X = ls[["GDP per capita (USD)"]].values
y = ls[["Life satisfaction"]].values
# print(X)

#grid = True -> 그래프 뒤에 격자 등장 .
# ls.plot(kind="scatter", grid = True, x = "GDP per capita (USD)", y = "Life satisfaction")
# plt.axis([23500,62500,4,9]) #그래프 축 범위 설정
# plt.show()


# 모델 선택
# model = LinearRegression() #LinearRegression 모델
model = KNeighborsRegressor(n_neighbors=3) # KNeighborsRegressor 모델

model.fit(X,y)

# X_new = [[37655.2]] # 예측해서 x에 넣을 값
X_new = [[31721.3]]
print(model.predict(X_new))
#LinerRegression 5.90
#KNeighborRegressor 5.70