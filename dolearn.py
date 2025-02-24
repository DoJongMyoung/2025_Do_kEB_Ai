import numpy as np
import pandas as pd


class KNeighborsRegressor:
    def __init__(self, n_neighbors = 5): #입력안하면 디폴트 값 5로 설정
        self.n_neighbors = n_neighbors



    def sort(self, Df, X):
        col_2 = Df.iloc[:, [1]].values.tolist() #2번째 세로줄
        col_3 = Df.iloc[:, [2]].values.tolist() #3번째 세로줄
        abs_list = [] # 절대값을 받을 리스트

        #절대값을 넣을 for문
        for i in col_2:
            abs_list.append(abs(i[0] - X)) #abs 리스트에 추가 완료

        rows, cols = Df.shape # 길이를 알아내기 위함

        new_list = [] #GDP를 절대값으로 차로 바꾼 리스트

        for i in range(0,rows):
            new_list.append([abs_list[i], col_3[i]])

        new_list.sort(key=lambda x: x[0])
        return new_list


    def fit(self, X, y):

        pass

    def predict(self, sorted_list) -> np.ndarray:

        happy = 0
        print(sorted_list)
        for i in range(self.n_neighbors):
            happy = happy + float(sorted_list[i][1][0])

        happy = happy / self.n_neighbors

        return happy

#predict를 사용하면 n_neighbors= k만큼 가까운 수 에서 뽑은 수들을 뽑아 평균을 냄.

