import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	"""
	Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	Args:
		data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.

	"""
	# Your code here
	result = []

	for i in range(len(data)):
		pseudo = []
		for j in range(degree+1):
			temp = data[i]**j
			pseudo.append(temp)
		result.append(pseudo)
	return result
