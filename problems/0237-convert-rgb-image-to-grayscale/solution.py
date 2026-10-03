import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    # Write your code here

    arr = np.array(image)
    if len(arr.shape) != 3:
        return -1
    
    gray_scale = []

    for i in range(len(image)):
        temp_list = []
        temp = 0
        for j in range(len(image[0])):
            if image[i][j][0] > 255 or image[i][j][1] > 255 or image[i][j][2] > 255:
                return -1
            temp = 0.299*image[i][j][0] + 0.587*image[i][j][1] + 0.114*image[i][j][2]
            temp_list.append(round(temp, 0))
        gray_scale.append(temp_list)

    return gray_scale
    
                
                









