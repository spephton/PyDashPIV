import numpy as np

def gauss(A): # reduces an augmented matrix, A, to a gaussian echelon form. A is a numpy float ndarray, assumed to have n rows and m entries in each row, m > n, does not test m and n assumptions.
	
	if (A.dtype != 'f'):
		print('ERROR: input ndarray must be of type "float"')
		return
	
	
	
	pivotFoundInColumn = np.zeros(len(A[0]))

	for pivot in range (len(A)):
		for i in range(pivot, len(A)): # swap rows so first nonzero entry in column occurs at pivot row
			if A[i][pivot] != 0:
				pivotFoundInColumn[pivot] = 1	# can optimise here, we know col pivot is zero 	in rows pivot through i
				if i == pivot:
					break # the pivot row is in the right spot
				elif i > pivot:
					currentPivotRow = A[pivot] # swap row i with pivot row. first store row.
					A[pivot] = A[i] # put the i'th row in the pivot row
					A[i] = currentPivotRow # and put stored row in the i'th row
				else:
					print("error, somehow considering a row above the pivot")
				
	

		if pivotFoundInColumn[pivot]: 	# the column has a non-zero entry, (and that entry is in the pivot row)
			pivVal = A[pivot][pivot]
			for i in range(pivot + 1, len(A)): 	# all rows under pivot: row ops to zero the 	pivot column entry
				if A[i][pivot]:
					ratio = pivVal/A[i][pivot]
					A[i] = A[pivot] - ratio*A[i]
				
	




def jordan(A): # row-reduces an augmented matrix in echelon form, A, to reduced echelon form. A is a numpy float ndarray, assumed to have n rows and m columns, m > n. Tests input only for type.
	
	if (A.dtype != 'f'):
		print('ERROR: input ndarray must be of type "float"')
		return
	
	for rowNumber in range(len(A)): # row ops to make every pivot 1
		if (pivot := A[rowNumber][rowNumber]) != 0:
			A[rowNumber] = A[rowNumber] / pivot
	
	for subSourceRowNumber in range(len(A) - 1, 0, -1):
		for targetRowNumber in range(0, subSourceRowNumber):
			if (targetRowSubColumnValue := A[targetRowNumber][subSourceRowNumber]) != 0:
				A[targetRowNumber] = A[targetRowNumber] - targetRowSubColumnValue * A[subSourceRowNumber]
			
def gaussJordan(A):
	gauss(A)
	jordan(A)


				

			
# tests

B = np.array( [ [2, 1, 1, 5],
				[4, 1, 3, 9],
				[-2, 2, 1, 8]], dtype = 'f')
gaussJordan(B)
#print(B) # passed
# Expect: 1 0 0 0
#		  0 1 0 3
#		  0 0 1 2
				
C = np.array([1, 0, 1])
# Expect: type error

D = np.array([[2, 1, 4],
				[4, 1, 7]], dtype = 'f')
#gauss(D)
#print(D)
#jordan(D)
#print(D)
# Expect: 1 0 1.5
#		  0 1 1 	Passed

E = np.array([[2, 1, 4], 
			[4, 2, 8]], dtype = 'f')
# gauss(E)
# print(E)
# jordan(E)
# print(E)
# Expect 1 0.5 2
#		 0	0  0	Passed. This is a consistent system with infinitely many solutions


F = np.array([[2, 1, 4], [4, 2, 0]], dtype = 'f')
# gauss(F)
# print(F)
# jordan(F)
# print(F)
# Expect 1 0.5 0
#		 0  0  4	Passed. This is an inconsistent system and hence there are no solutions, and we can't trust this output to mean anything (since it says 0 = 4)
