import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	
	det_T = np.linalg.det(T)
	det_S = np.linalg.det(S)

	if det_T == 0 or det_S == 0:
		return -1

	else:
		inv_T = np.linalg.inv(T)
		T_inv_A = np.dot(inv_T, A)
		return np.dot(T_inv_A, S)

	# return transformed_matrix