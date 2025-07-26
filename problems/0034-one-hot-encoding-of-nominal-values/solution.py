import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
    unique_cat = set(x)
    if n_col == None: unique_cat = set(x)
    else: no_cat = n_col

    no_cat = len(unique_cat) if n_col is None else n_col


    vector = np.zeros(no_cat)

    ans = []
    for i in range(len(x)):
        pos = 0
        for j in unique_cat:
            if x[i] == j:
                pos = j
        vector[pos] = 1
        ans.append(vector)
        vector = np.zeros(no_cat)


    return ans