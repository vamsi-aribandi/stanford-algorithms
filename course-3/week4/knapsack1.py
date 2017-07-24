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
	Function to find value of knapsack, with space O(mn), where
	m = max weight allowed
	n = no. of items
	Use for small inputs where reconstructing final set matters
	"""
	solutions = [[None for i in range(kSize + 1)] for i in range(n + 1)]
	for x in range(kSize + 1):
		solutions[0][x] = 0
	for i in range(1, n + 1):
		value, weight = iList[i]
		for x in range(kSize + 1):
			if weight > x:
				solutions[i][x] = solutions[i - 1][x]
			else:
				solutions[i][x] = max(solutions[i - 1][x], solutions[i - 1][x - weight] + value)
	return reconstruct(solutions, n, kSize, iList), solutions[n][kSize]

def reconstruct(solutions, n, kSize, iList):
	"""
	reconstruct(solutions, n, kSize, iList):
	Function to return a set of all items in original knapsack problem,
	given the solutions of its subproblems.
	"""
	s = set()
	i, x = n, kSize
	while x > 0 and i > 0:
		value, weight = iList[i]
		if weight > x or solutions[i - 1][x] > solutions[i - 1][x - weight] + value:
			pass
		else:
			x -= weight
			s.add(i)
		i -= 1
	return s

main()