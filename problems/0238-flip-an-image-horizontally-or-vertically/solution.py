import numpy as np

def flip_image(image, direction):
    """
    Flip an image horizontally or vertically.
    
    Args:
        image: 2D or 3D list/array representing a grayscale or RGB image
        direction: string, either 'horizontal' or 'vertical'
    
    Returns:
        Flipped image as a nested list, or -1 if input is invalid
    """
    # Your code here
    arr = np.array(image)
    if len(arr.shape) != 2 and len(arr.shape) != 3:
        return -1
    
    if direction not in ['horizontal', 'vertical']:
        return -1

    if direction == 'horizontal':
        return arr[:, ::-1]
    else:
        return arr[::-1, :]
     

    






