import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	inverse = np.linalg.inv(matrix)
	return inverse