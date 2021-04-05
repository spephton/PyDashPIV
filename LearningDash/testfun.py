import numpy

def testfun(x):
	x += 10
	return x
	
a = 6

b = numpy.array([6])

testfun(a)
testfun(b)

print(a)
print(b)