import heapq

def main():
	with open('test.txt') as f:
		numbers = []
		for line in f:
			numbers.append(int(line))
	print(sum_medians(numbers))

def sum_medians(numbers):
	"""
	sum_medians(numbers):
	Function to return the sum of continuously added medians given a list of numbers,
	using the function push_and_get_median
	"""
	result = 0
	heapLow, heapHigh = [], []
	for n in numbers:
		result += push_and_get_median(heapLow, heapHigh, n)
	return result

def push_and_get_median(heapLow, heapHigh, n):
	"""
	push_and_get_median(heapLow, heapHigh, n):
	Function to add n to the numbers and return the median,
	using heaps of lower and higher values.
	"""
	lowLen, highLen = len(heapLow), len(heapHigh)
	if lowLen == highLen == 0: # for when both heaps are empty
		heapq.heappush(heapLow, -n)
		return n
	elif highLen > lowLen:
		if n > heapHigh[0]: # make sure heaps aren't unbalanced
			heapq.heappush(heapLow, -heapq.heappop(heapHigh))
			heapq.heappush(heapHigh, n)
		else:
			heapq.heappush(heapLow, -n)
		return -heapLow[0]
	elif highLen < lowLen:
		if n < -heapLow[0]: # make sure heaps aren't unbalanced
			heapq.heappush(heapHigh, -heapq.heappop(heapLow))
			heapq.heappush(heapLow, -n)
		else:
			heapq.heappush(heapHigh, n)
		return -heapLow[0]
	else: # sizes are equal, heaps won't get unbalanced
		if n < -heapLow[0]:
			heapq.heappush(heapLow, -n)
			return -heapLow[0]
		else:
			heapq.heappush(heapHigh, n)
			return heapHigh[0]

main()