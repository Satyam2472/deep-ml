def phi_corr(x: list[int], y: list[int]) -> float:
	"""
	Calculate the Phi coefficient between two binary variables.

	Args:
	x (list[int]): A list of binary values (0 or 1).
	y (list[int]): A list of binary values (0 or 1).

	Returns:
	float: The Phi coefficient rounded to 4 decimal places.
	"""
	# Your code here
	val = 0

    x00 = 0
    x01 = 0
    x10 = 0
    x11 = 0

    for i in range(len(x)):
        if x[i] == 0 and y[i] == 0: x00 += 1
        elif x[i] == 0 and y[i] == 1: x01 += 1
        elif x[i] == 1 and y[i] == 0: x10 += 1
        else: x11 += 1
    
    val = ((x00*x11)-(x01*x10))/(((x00+x01)*(x10+x11)*(x00+x10)*(x01+x11))**0.5)


	return round(val,4)