
import numpy as np
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""

    v = np.array(v)
    L = np.array(L)

	v_dot_L = np.dot(v, L.T)
    L_dot_L = np.dot(L, L.T)

    factor = round(v_dot_L/L_dot_L, 3)
    return factor*L

