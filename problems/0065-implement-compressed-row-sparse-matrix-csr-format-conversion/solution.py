import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	vals = []
    col_idx = []
    row_ptr = []
    row_count = 0
    row_ptr.append(row_count)

    for i in range(len(dense_matrix)):
        for j in range(len(dense_matrix[0])):
            if dense_matrix[i][j] != 0:
                vals.append(dense_matrix[i][j])
                col_idx.append(j)
                row_count += 1
        row_ptr.append(row_count)

    return vals, col_idx, row_ptr

