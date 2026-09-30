import string
import re

def exact_match_score(predictions: list[str], references: list[str]) -> float:
    """
    Calculate the exact match score between predictions and references.
    
    Args:
        predictions: List of predicted strings
        references: List of reference (ground truth) strings
    
    Returns:
        Exact match score as a float between 0 and 1
    """
    # Your code here
    if len(predictions) == 0 or len(references) == 0: return 0.0

    correct = 0

    for i in range(len(predictions)):

        # normalization
        predictions[i] = predictions[i].lower()
        references[i] = references[i].lower()

        # remove any special characters
        predictions[i] = re.sub(r'[^a-zA-Z0-9\s]', '', predictions[i])

        # remove any extra spaces if there from between the characters
        predictions[i] = re.sub(r'\s+', ' ', predictions[i])

        # trim the extra spaces from both the ends
        predictions[i] = predictions[i].strip()

    for i in range(len(predictions)):
        if predictions[i] == references[i]: correct += 1

    return correct/len(predictions)




