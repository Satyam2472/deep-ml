
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	rmse_res = 0
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)

	# for i in range(len(y_true)):
	# 	rmse_res += (y_true[i] - y_pred[i])**2
	rmse_res = np.mean((y_true - y_pred)**2)
	
	rmse_value = np.sqrt(rmse_res)

	return round(rmse_value,3)
