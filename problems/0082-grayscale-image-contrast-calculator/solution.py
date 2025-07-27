import numpy as np

def calculate_contrast(img) -> int:
	"""
	Calculate the contrast of a grayscale image.
	Args:
		img (numpy.ndarray): 2D array representing a grayscale image with pixel values between 0 and 255.
	"""
	# Your code here
	max_val = -300
    min_val = 500

    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] < min_val:
                min_val = img[i][j]
            if img[i][j] > max_val:
                max_val = img[i][j]
    return max_val - min_val