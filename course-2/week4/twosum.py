def main():
	numberSet = set()
	numberList = []
	with open('test.txt') as f:
		for line in f:
			numberSet.add(int(line))
			numberList.append(int(line))
	low = 3 # -10000 for algo1-programming_prob-2sum, 3 for test
	high = 10 # 10000 for algo1-programming_prob-2sum, 10 for test
	print(count_twosum(numberList, numberSet, low, high))

def count_twosum(numberList, numberSet, low, high):
	"""
	count_twosum(numberList, numberSet, low, high):
	Function to return number of values t in [low, high] (inclusive),
	such that there exist distinct x,y where x + y = t, using a hashtable
	(checking if a value is in a python set is similar to that of a dict in python i.e. hashtable)
	numberList exists because traversing through a list is faster than a set
	"""
	count = 0
	for t in range(low, high + 1):
		for x in numberList:
			y = t - x
			if y in numberSet and y != x:
				count += 1
				break
	return count

main()