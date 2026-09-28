import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    # Your code here
    if len(p) != len(q) or len(p) == 0 or len(q) == 0:
        return 0.0

    else:
        temp_sum = 0
        for i in range(len(p)):
            temp_sum += (p[i]*q[i])**0.5
        return np.round((-1)*np.log(temp_sum), 4)