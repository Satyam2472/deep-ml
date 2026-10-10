import numpy as np

def he_initialization(n_in: int, n_out: int, mode: str = 'fan_in', distribution: str = 'uniform', seed: int = None) -> np.ndarray:
    """
    Initialize weights using He (Kaiming) initialization.
    
    Parameters:
    - n_in: Number of input units (fan_in)
    - n_out: Number of output units (fan_out)
    - mode: 'fan_in' or 'fan_out'
    - distribution: 'normal' or 'uniform'
    - seed: Optional random seed for reproducibility
    
    Returns:
    - NumPy array of shape (n_in, n_out) containing the initialized weights.
    """
    if seed is not None:
        np.random.seed(seed)
        
    # Determine the fan dimension
    if mode == 'fan_in':
        fan = n_in
    elif mode == 'fan_out':
        fan = n_out
    else:
        raise ValueError("mode must be either 'fan_in' or 'fan_out'")
        
    if distribution == 'normal':
        # Standard deviation: std = sqrt(2 / fan)
        std = np.sqrt(2.0 / fan)
        weights = np.random.normal(loc=0.0, scale=std, size=(n_in, n_out))
        
    elif distribution == 'uniform':
        # Bound: limit = sqrt(6 / fan)
        limit = np.sqrt(6.0 / fan)
        weights = np.random.uniform(low=-limit, high=limit, size=(n_in, n_out))
        
    else:
        raise ValueError("distribution must be either 'normal' or 'uniform'")
        
    return weights