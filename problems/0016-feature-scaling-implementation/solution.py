import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	standardized_data = []
	normalized_data = []

	data_row = len(data)
	data_column = len(data[0])
	pseudo = []

	# standardization
	for i in range(data_row):
		for j in range(data_column):
			col_max = np.max(data[:, j])
			col_min = np.min(data[:, j])

			x_norm = round((data[i][j] - col_min)/(col_max - col_min), 4)
			pseudo.append(x_norm)

		normalized_data.append(pseudo)
		pseudo = []

	# normalization
	for i in range(data_row):
		for j in range(data_column):
			col_mean = np.mean(data[:, j])
			col_std = np.std(data[:, j])

			x_stand = round((data[i][j] - col_mean)/col_std, 4)

			pseudo.append(x_stand)

		standardized_data.append(pseudo)
		pseudo = []
	
	return standardized_data, normalized_data