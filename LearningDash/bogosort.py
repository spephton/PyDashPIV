import random

def main():
	list10 = list(range(10))
	random.shuffle(list10)
	list100 = list(range(100))
	random.shuffle(list100)
	print(list10)
	print(bogo_sort(list10))
	print(list100)
	print(bogo_sort(list100))

def is_sorted(list):
	if len(list) > 1:
		for i in range(len(list) - 1):
			if list[i] > list[i+1]:
				return False
	return True

def bogo_sort(list):
	while not is_sorted(list):
		random.shuffle(list)
	return list
		
if __name__ == '__main__':
	main()