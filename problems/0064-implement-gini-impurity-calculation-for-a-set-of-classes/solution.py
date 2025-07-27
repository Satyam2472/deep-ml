
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	
    total = len(y)
    ele_dict = {}

    for i in y:
        if i not in ele_dict:
            ele_dict[i] = 1
        else:
            ele_dict[i] += 1
    
    temp = 0
    for key, value in ele_dict.items():
        temp += (value/total)**2
    return round(1-temp, 3)