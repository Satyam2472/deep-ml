
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)

	y_true_mean = np.mean(y_true)

	ssr = np.sum((y_true - y_pred)**2)
	sst = np.sum((y_true - y_true_mean)**2)

	return round((1-ssr/sst), 3)