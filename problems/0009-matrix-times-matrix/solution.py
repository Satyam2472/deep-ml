import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
	col_a = len(a[0])
	row_b = len(b)

	if col_a != row_b:
		return -1
	else:
		return np.dot(a, b)
	