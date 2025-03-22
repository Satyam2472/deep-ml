import numpy as np
def min_max(x: list[int]) -> list[float]:
	# Your code here
	x_min = np.min(x)
	x_max = np.max(x)
	

	for i in range(len(x)):
		if x_min == x_max:
			x[i] = 0
		else:
			x[i] = (x[i] - x_min)/(x_max - x_min)
	
	return x
	