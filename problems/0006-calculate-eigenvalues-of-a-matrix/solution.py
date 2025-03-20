import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	row = len(matrix)
	matrix = np.array(matrix)

	determinant = np.linalg.det(matrix)
	trace = 0
	for i in range(row):
		trace += matrix[i][i]
	
	lambda_1 = (trace - np.sqrt(trace**2 - 4*determinant))/2
	lambda_2 = (trace + np.sqrt(trace**2 - 4*determinant))/2

	eigenvalues = []
	eigenvalues.append(round(lambda_2, 1))
	eigenvalues.append(round(lambda_1, 1))

	return eigenvalues