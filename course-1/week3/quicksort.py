# import random

def main():
	numbers = []
	with open("test.txt") as f:
		for line in f:
			numbers.append(int(line))
	# print("original: {}".format(numbers))
	print(quicksort(numbers, 0, len(numbers) - 1))
	# print("sorted:   {}".format(numbers))

def quicksort(numbers, left, right):
	"""
	quicksort(numbers, left, right):
	Function to recursively sort a part of list given the part's left and right limits(inclusive).
	returns no. of comparisons required to do so(including that of children in recursion tree)
	"""
	if right > left:
		# oldPivotIndex = random.randint(left, right)
		oldPivotIndex = median_of_three(numbers, left, right) # change this line accordingly to find answers for different pivots
		newPivotIndex = partition(numbers, left, right, oldPivotIndex)
		count = quicksort(numbers, left, newPivotIndex - 1)
		count += quicksort(numbers, newPivotIndex + 1, right)
		return count + right - left
	else:
		return 0

def partition(numbers, left, right, PivotIndex):
	"""
	partition(numbers, left, right, PivotIndex):
	Function to partition a part of a list about element at `PivotIndex` given the part's left and right limits(inclusive),
	as well as return the final position of pivot element.
	"""
	numbers[left], numbers[PivotIndex] = numbers[PivotIndex], numbers[left] # put pivot element at the left
	i = left
	for j in range(left + 1, right + 1):
		if numbers[j] < numbers[left]:
			numbers[j], numbers[i + 1] = numbers[i + 1], numbers[j]
			i += 1
	numbers[left], numbers[i] = numbers[i], numbers[left] # return pivot element from leftmost index to correct position
	return i

def median_of_three(numbers, left, right):
	"""
	median_of_three(numbers, left, right):
	FUnction to return the position of the median of the left element, right element and middle element of numbers[left:right]
	"""
	mid = (left + right) // 2
	items = [(numbers[left], left), (numbers[right], right), (numbers[mid], mid)]
	return sorted(items)[1][1]

main()