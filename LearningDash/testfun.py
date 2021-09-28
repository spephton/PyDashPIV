import numpy

def testfun(x):
	x += 10
	return x
	
a = 6

b = numpy.array([6])

testfun(a)
testfun(b)

print(a) # 6, pass by assignment, x within the function has it's reference changed to 16 and is returned, but a outside the function does not have it's reference changed
print(b) # [16], numpy.array is passed by reference, so x becomes a reference to the same array that a is a reference to. When the += operator is used, the array is modified in place, assignment happens for the elements but not the array itself

def testfun2(x): 
	x = x + 10
	return x

def testfun3(x):
	x[1] = x[1] + 10
	return x

# testfun2 is assigning a new piece of data: the right hand side, to x. Therefore, x is assigned to a different piece of data within the function, leaving the data it was originally referencing alone. 

# testfun3, otoh, assigns a new value only to an *element* of x. Since the reference to the array itself isn't changing, only this element's reference, the reference in the original array that both x and a refer to changes as well. 

c = numpy.array([1, 3, 5])

testfun2(c) 
print(c)	# 1 3 5
testfun3(c)
print(c)	# 1 13 5

# So, how do we modify array elements without changing the original array? We could try doing something like in testfun2 