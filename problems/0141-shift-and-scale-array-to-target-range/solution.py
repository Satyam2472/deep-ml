import numpy as np

def convert_range(values: np.ndarray, c: float, d: float) -> np.ndarray:
    """
    Shift and scale values from their original range [min, max] to a target [c, d] range.
    """
    # Your code here
    a = np.min(values)
    b = np.max(values)
    
    # Handle the edge case where all values in the array are identical
    if a == b:
        return np.full_like(values, c, dtype=float)
    
    return c + ((d - c) / (b - a)) * (values.astype(float) - a)