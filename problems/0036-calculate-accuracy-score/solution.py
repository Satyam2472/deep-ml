import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
    correct_count = 0
    for i in range(len(y_true)):
        if y_pred[i] == y_true[i]: 
            correct_count += 1
    
    return correct_count/len(y_true)