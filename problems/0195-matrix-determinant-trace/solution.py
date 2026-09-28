import numpy as np
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	determinant = np.round(np.linalg.det(matrix), 1)
	trace = 0
	rows, cols = len(matrix[0]), len(matrix[0])
	for i in range(rows):
		trace += matrix[i][i]

	return (determinant, trace)
