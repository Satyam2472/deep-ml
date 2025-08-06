import numpy as np


def swish(x: float) -> float:
	"""
	Implements the Swish activation function.

	Args:
		x: Input value

	Returns:
		The Swish activation value
	"""
	sigmoid = 1/(1+np.exp(-x))

	return x*sigmoid