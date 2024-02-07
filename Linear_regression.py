import numpy as np
from sklearn.linear_model import LinearRegression


def regressionLine(x,y):

    model = LinearRegression().fit(np.array(x).reshape(-1, 1),y)

    return f"({round(model.intercept_,4)}, {round(model.coef_[0],4)})"



