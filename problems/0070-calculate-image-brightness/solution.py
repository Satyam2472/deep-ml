
def calculate_brightness(img):
	# Write your code here
    
    row = len(img)
    # edge case 1
    if len(img) == 0:
        return -1
    col = len(img[0])

    # edge case 2
    for i in range(row):
        if len(img[i]) != col:
            return -1

    brightness = 0

    for i in range(row):
        for j in range(col):
            # edge case 3
            if img[i][j] > 255 or img[i][j] < 0:
                return -1
            brightness += img[i][j]
    
    return round(brightness/(row*col), 2)
