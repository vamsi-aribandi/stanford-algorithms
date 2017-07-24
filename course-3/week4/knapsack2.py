def main():
	iList = [None]
	with open('test.txt') as f:
		firstLine = f.readline().split(' ')
		kSize, n = int(firstLine[0]), int(firstLine[1])
		for line in f:
			tempList = line.split(' ')
			iList.append((int(tempList[0]), int(tempList[1])))
	print(knapsack(n, kSize, iList))

def knapsack(n, kSize, iList):
	"""
	knapsack(n, kSize, iList):
	Function to find max value of knapsack, with space O(m), where
	m = max weight allowed
	Use for huge inputs, where reconstructing final set doesn't matter
	"""
	solutions = [[None for i in range(kSize + 1)] for i in range(2)]
	for x in range(kSize + 1):
		solutions[0][x] = 0
	for i in range(1, n + 1):
		value, weight = iList[i]
		for x in range(kSize + 1):
			if weight > x:
				solutions[1][x] = solutions[0][x]
			else:
				solutions[1][x] = max(solutions[0][x], solutions[0][x - weight] + value)
		solutions[0] = solutions[1].copy()
	return solutions[1][kSize]

main()