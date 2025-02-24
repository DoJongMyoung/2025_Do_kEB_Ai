import numpy as np

class LinearRegression:
    def __init__(self):
        self.slope = None # 기울기
        self.intercept = None # 절편

    def fit(self, X, y):
        """
        learning function
        :param X: independent variable (2d array format)
        :param y: dependent variable (2d array format)
        :return: none
        """
        X_mean = np.mean(X)
        y_mean = np.mean(y)

        denominator = np.sum(pow(X_mean, 2))
        numerator = np.sum((X - X_mean) * (y - y_mean))

        self.slope = numerator / denominator
        self.intercept = y_mean - (self.slope * X_mean)

    def predict(self, X) -> np.ndarray:
        """
        predict value for input
        :param X: new indepent variable
        :return: predict value for input (2d array format)
        """
        return self.slope * np.array(X) + self.intercept