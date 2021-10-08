import numpy as np

def correlation(signal1, signal2):
	'''Cross-correlate two discrete-uniform signals with each other. 
	
	Returns array of correlation strength where entry n has the correlation strength of signal 2 with signal 1 after signal 2 has been shifted n steps right (with wraparound) (NOTE not totally happy with this explanation)'''
	
	len1 = len(signal1)
	len2 = len(signal2)
	
	# add zeros to allow for signal translation across full range of possible overlaps
	# you can optimise here by reducing the number of zeros if you assume that correlation occurs somewhere in the middle, which will save more clocks for bigger signals
	signal1 = np.concatenate((signal1, np.zeros(len2)))
	signal2 = np.concatenate((signal2, np.zeros(len1)))
	
	correlation = np.empty(len1 + len2)
	
	for i in range(len1+len2):
		correlation[i] = sum(signal1 * np.concatenate((
			signal2[i:],
			signal2[:i]
			))
		)
	
	return correlation


print(correlation(np.array([1, 1, 3, 6, 2, 3, 1, 0]),np.array([1, 2, 7, 1])))