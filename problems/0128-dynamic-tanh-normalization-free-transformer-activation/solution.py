import numpy as np

def dynamic_tanh(x: np.ndarray, alpha: float, gamma: float, beta: float) -> np.ndarray:
    tanh_val = (np.exp(alpha * x) - np.exp(-alpha * x)) / (np.exp(alpha * x) + np.exp(-alpha * x))
    return gamma * tanh_val + beta