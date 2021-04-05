import numpy as np

def gauss(A): # Returns the gaussian echelon form of an augmented matrix A. A is a numpy float ndarray, assumed to have n rows and m entries in each row, m > n, does not test m and n assumptions.
	
	if (A.dtype != 'f'):
		print('ERROR: input ndarray must be of type "float"')
	
	
	
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
				
	
				

			
# tests

B = np.array( [ [2, 1, 1, 5],
				[4, 1, 3, 9],
				[-2, 2, 1, 8]], dtype = 'f')
				
gauss(B)

print(B)