argumentList = [[1,2], [3, 4]]

def myFunc(a, b, c, d):
	print(d, c, b, a)

#myFunc(*argumentList) # doesn't work. Function sees a = [1,2], b = [3, 4], c & d missing.

#myFunc(*(*argumentList)) # syntax errors