import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	
	# Your code here
	r1 = np.dot(X, weights.T)
	r2 = r1 + bias
	predictions = []
	for i in range(len(r2)):
		a1 = 1/(1+np.exp(r2[i]))
		if a1 > 0.5:
			predictions.append(0)
		else:
			predictions.append(1)
    
	return predictions
        