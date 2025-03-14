def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	
	result = []
	pseudo = []
	counter = 0

	a_row = len(a)
	a_column = len(a[0])

	flattened_list = []
	for i in range(a_column):
		for j in range(a_row):
			flattened_list.append(a[j][i])

	for i in range(a_column):
		for j in range(a_row):
			pseudo.append(flattened_list[counter])
			counter += 1
		
		result.append(pseudo)
		pseudo = []

	return result


	
	# return b