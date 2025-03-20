import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	
	X = np.array(X)
	y = np.array(y).reshape(-1, 1)
	
	a1 = np.dot(X.T, X)
	a2 = np.linalg.inv(a1)
	a3 = np.dot(a2, X.T)
	a4 = np.dot(a3, y)
	
	return a4
	