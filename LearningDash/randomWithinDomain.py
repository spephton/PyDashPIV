import numpy as np

def randomWithinDomain(xDomain, yDomain, nSamples):
	'''Generate array containing n uniformly randomly placed points within the 2d domain given. xDomain and yDomain are two-element lists specifying the minimum and maximum x and y values respectively'''
	xSourceValues = np.random.rand(nSamples)
	x = xSourceValues * (xDomain[1]-xDomain[0]) + xDomain[0]
	
	ySourceValues = np.random.rand(nSamples)
	y = ySourceValues * (yDomain[1] - yDomain[0]) +yDomain[0]
	
	return x, y
	
x, y  = randomWithinDomain([-3,3], [3, 9], 20)

print(f'x = {x}')
print(f'y = {y}')

z, aa = randomWithinDomain([-9, -3], [3, -3], 20)

print(f'z = {z}')
print(f'aa = {aa}')