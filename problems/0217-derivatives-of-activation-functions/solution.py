import math as m
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	# Your code here
	ans = {'sigmoid': 0.00, 'tanh': 0.00, 'relu': 0.00}

	if x > 0:
		ans['relu'] = 1
	else:
		ans['relu'] = 0

	tanh = (m.exp(x) - m.exp(-x))/(m.exp(x) + m.exp(-x))
	ans['tanh'] = 1 - tanh**2

	sigmoid = 1/(1+m.exp(-x))

	ans['sigmoid'] = sigmoid*(1-sigmoid)

	return ans

	