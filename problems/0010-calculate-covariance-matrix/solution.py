import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	arr = np.array(vectors)
    cov_matrix = np.cov(arr)  # Treat columns as variables
    return cov_matrix.tolist()