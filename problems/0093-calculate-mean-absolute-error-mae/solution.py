import numpy as np

def mae(y_true, y_pred):
	
    val = np.mean(abs(y_true - y_pred))
	
    return round(val,3)