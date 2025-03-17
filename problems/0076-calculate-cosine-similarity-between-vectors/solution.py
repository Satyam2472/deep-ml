
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
	v1_dot_v2 = np.dot(v1, v2)
	v1_square_sqrt = np.sqrt(np.dot(v1, v1))
	v2_square_sqrt = np.sqrt(np.dot(v2, v2))

	result = v1_dot_v2/(v1_square_sqrt*v2_square_sqrt)
	return round(result, 3)

