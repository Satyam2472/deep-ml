
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	tp = 0
	fp = 0
	fn = 0

	for i in range(len(y_true)):
		if y_true[i] == 1 and y_pred[i] == 1:
			tp += 1
		elif y_true[i] == 0 and y_pred[i] == 1:
			fp += 1
		elif y_true[i] == 1 and y_pred[i] == 0:
			fn += 1
		else:
			continue
	if (tp + fp + fn) == 0: return float(0)
	dice_score = (2*tp)/(2*tp+fp+fn)
	return round(dice_score, 3)
