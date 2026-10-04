import numpy as np

def zero_pad_image(img, pad_width):
    # 1. Handle negative or zero pad_width
    if pad_width < 0:
        return -1
    if pad_width == 0:
        return img

    # 2. Handle empty input
    if not img or len(img) == 0:
        return -1

    # 3. Handle 1D input or non-list/non-sequence rows
    if not isinstance(img[0], list) and not isinstance(img[0], np.ndarray):
        return -1

    # 4. Handle empty 2D rows (e.g., [[]])
    if len(img[0]) == 0:
        return -1

    # --- Standard Padding Logic ---
    
    # If working with Python lists:
    # Note: Use list copies [0] * num_cols so rows don't share the same reference memory
    num_cols = len(img[0]) + 2 * pad_width

    for row in img:
        # Add zeros left and right
        row[:0] = [0] * pad_width
        row.extend([0] * pad_width)

    # Add zeros top and bottom
    for _ in range(pad_width):
        img.insert(0, [0] * num_cols)
        img.append([0] * num_cols)

    return img