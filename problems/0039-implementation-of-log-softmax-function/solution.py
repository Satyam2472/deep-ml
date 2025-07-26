import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	exp_sum = 0
    for i in scores:
        exp_sum += np.exp(i)
    
    ans = []
    for i in scores:
        temp = np.log(np.exp(i)/exp_sum)
        ans.append(temp)
    return ans