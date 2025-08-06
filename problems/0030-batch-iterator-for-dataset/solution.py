import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	n_samples = len(X)
    indices = np.arange(n_samples)

    batch = []

    for start_idx in range(0, n_samples, batch_size):
        
        batch_idx = indices[start_idx: start_idx + batch_size]
        
        X_batch = X[batch_idx].tolist()
        if y is not None:
            y_batch = y[batch_idx].tolist()
            batch.append([X_batch, y_batch])
        else:
            batch.append(X_batch)
        
    return batch