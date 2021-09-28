# -*- coding: utf-8 -*- (bbedit default i think)

import numpy as np

# function definitions

# velocity field function returns velocity at a point specified by position vector
constantVelocity = np.array([1,2], dtype = 'f')

def constantVField(position):
	return constantVelocity

# return a velocity field array in a square range from squareRange[0] to squareRange[1], with resolution entries over that range
def makeVArray(squareRange, resolution):
	"""Return a velocity field array that spans 'squareRange' on both x and y, with 'resolution' samples """
	# NOTE: for np.arrays, appending is fast whereas prepending is slow
	
	xArray = np.empty((0, resolution, 2))
	vArray = np.empty((0, resolution, 2))

	
	columns = resolution
	rows = resolution
	delta = (squareRange[1] - squareRange[0])/resolution
	# define array such that can recall entries using array[x_n][y_n]	
	for i in np.linspace(squareRange[0], squareRange[1], columns):
		currentColumnX = np.empty((1, 0, 2))
		currentColumnV = np.empty((1, 0, 2))
		for j in np.linspace(squareRange[0], squareRange[1], rows):
			currentX = np.array([[[i, j]]], dtype = 'f')
			currentV = np.array([[constantVField(currentX)]])
			currentColumnX = np.concatenate((currentColumnX, currentX), axis = 1) #append current x to current column
			currentColumnV = np.concatenate((currentColumnV, currentV), axis = 1)
		vArray = np.concatenate((vArray, currentColumnV), axis = 0)
		xArray = np.concatenate((xArray, currentColumnX), axis = 0)
		
	return vArray, xArray # returns tuple containing both arrays
	
	
# "main"
v, x = makeVArray(np.array([-3, 3], dtype = 'f'), resolution = 11)#
print(v)
print(x)

# Can use np.meshgrid to create xy grid

"""x = np.linspace(-3, 3, 11)
y = np.linspace(-3, 3, 11)
print(x)
print(y)
alternative = np.meshgrid(x, y)
print(alternative)"""

