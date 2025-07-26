import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	y_hat = []

    # calculate the predictions
    for i in X:
        xi = i.T
        y_pred = np.dot(w, xi)
        y_hat.append(y_pred)

    # calculate the MSE
    error = 0
    for i in range(len(y_true)):
        error += (y_true[i] - y_hat[i])**2
    
    MSE = error/len(y_true)

    weight_sum = 0
    for i in w:
        weight_sum += i**2

    L = MSE + alpha*weight_sum
    return L
