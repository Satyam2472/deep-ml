
import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
	result = 0
    intersection = 0
    union = 0

    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            intersection += 1
            union += 1
        elif y_true[i] == 1 or y_pred[i] == 1:
            union += 1
        else:
            continue
    
    return round(intersection/union, 3)

