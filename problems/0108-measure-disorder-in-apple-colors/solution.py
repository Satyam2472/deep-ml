def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	# Your code here
	distinct = {}

    for i in apples:
        if i not in distinct:
            distinct[i] = 1
        else:
            distinct[i] += 1
    
    temp = 0
    for key, value in distinct.items():
        temp += (value/len(apples))**2
    
    return 1 - temp