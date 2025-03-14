import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	reshaped_matrix = []
	
	a_row = len(a)
	a_column = len(a[0])

	if a_row*a_column != new_shape[0]*new_shape[1]:
		return reshaped_matrix
	
	# flattening the matrix
	flattened_list = [item for sublist in a for item in sublist]


	pseudo = []
	counter = 0

	for i in range(new_shape[0]):
		for j in range(new_shape[1]):
			pseudo.append(flattened_list[counter])
			counter += 1
		
		reshaped_matrix.append(pseudo)
		pseudo = []

	return reshaped_matrix