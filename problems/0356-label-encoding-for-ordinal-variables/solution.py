def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    
    encoder = {}
    val = 0

    for i in order:
        encoder[i] = val
        val += 1
    
    ans = []

    for i in values:
        ans.append(encoder[i] if i in encoder else -1)
        

    return ans
