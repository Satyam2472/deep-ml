import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
	# Your code here
	ans = []

    height = len(x)
    width = len(x[0])
    div_factor = height*width

    for k in range(len(x[0][0])):
        sum_ = 0
        for i in range(len(x)):
            for j in range(len(x[0])):
                sum_ += x[i][j][k]
        
        ans.append(sum_/div_factor)
    
    ans = np.array(ans)
    return ans
