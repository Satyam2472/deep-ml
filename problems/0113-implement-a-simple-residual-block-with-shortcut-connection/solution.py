import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
	# Your code here
	a1 = w1@x
	# applying relu activation
	a1_act = []
	for i in a1:
		a1_act.append(max(i, 0))

	# layer 2
	a2 = w2@a1_act
	resnet = a2 + x
	# applying relu actiavtion
	a2_act = []
	for i in resnet:
		a2_act.append(max(i, 0))

	return a2_act
	

