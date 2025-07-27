def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	# Your code here
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
    
    if (tp+fp) != 0: precision = tp/(tp+fp)
    else: precision = 0

    if (tp+fn) != 0: recall = tp/(tp+fn)
    else: recall = 0

    if (precision+recall) != 0: f1 = 2*((precision*recall)/(precision+recall))
    else: f1 = 0.0
    return round(f1, 3)