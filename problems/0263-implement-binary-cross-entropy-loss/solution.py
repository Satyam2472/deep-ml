import math as m

def binary_cross_entropy(y_true: list[float], y_pred: list[float], epsilon: float = 1e-15) -> float:
	"""
	Compute binary cross-entropy loss.
	
	Args:
		y_true: True binary labels (0 or 1)
		y_pred: Predicted probabilities (between 0 and 1)
		epsilon: Small value for numerical stability
	
	Returns:
		Mean binary cross-entropy loss
	"""
	# Your code here
	loss = 0
	for i in range(len(y_pred)):
		if y_pred[i] == 0:
			y_pred[i] = epsilon
		elif y_pred[i] == 1:
			y_pred[i] = 1 - epsilon

		loss += -(y_true[i]*m.log(y_pred[i]) + (1-y_true[i])*m.log(1-y_pred[i]))

	return loss/len(y_pred)
	
