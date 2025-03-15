import math
import numpy as np

def sigmoid(z):
	return 1/(1 + np.exp(-z))

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):

	X = np.array(features)
	w = np.array(weights)
	y = np.array(labels)

	z = np.dot(X, w) + bias

	predictions = sigmoid(z)

	mse = np.mean((y - predictions)**2)

	predictions_rounded = np.round(predictions, 4).tolist()
	mse = round(mse, 4)

	return predictions_rounded, mse
