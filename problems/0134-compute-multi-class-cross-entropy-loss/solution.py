import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon: float = 1e-15) -> float:
    # Convert inputs to numpy arrays in case lists are passed
    y_pred = np.array(predicted_probs)
    y_true = np.array(true_labels)
    
    # Clip predicted probabilities to prevent log(0) numerical instability
    y_pred_clipped = np.clip(y_pred, epsilon, 1 - epsilon)
    
    # Compute cross-entropy loss per sample across classes
    # Categorical cross-entropy formula: -sum(y_true * log(y_pred))
    sample_losses = -np.sum(y_true * np.log(y_pred_clipped), axis=-1)
    
    # Return the average loss across all batch samples
    return float(np.mean(sample_losses))