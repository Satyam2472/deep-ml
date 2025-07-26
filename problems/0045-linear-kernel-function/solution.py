import numpy as np

def kernel_function(x1, x2):
	# Your code here
	inner_prod = 0
    for i in range(len(x1)):
        inner_prod += x1[i]*x2[i]
    return inner_prod
