def main():
	numbers = [56, 65, 23, 87, 2, 4, 76, 9, 0]
	print("Original: {}".format(numbers))
	mergesort(numbers)
	print("Sorted:   {}".format(numbers))

def mergesort(numbers):
	"""
	mergesort(numbers):
	Function that sorts a given list using merge sort.
	"""
	if len(numbers) > 1:
		mid = len(numbers) // 2
		left = numbers[:mid]
		right = numbers[mid:]
		mergesort(left)
		mergesort(right)
		merge(left, right, numbers)

def merge(left, right, numbers):
	"""
	merge(left, right, numbers):
	Function to merge two sorted lists.
	"""
	i, j, k = 0, 0, 0
	# merge until all elements of either left or right half have been stored in list in sorted order
	while i < len(left) and j < len(right):
		if left[i] > right[j]:
			numbers[k] = right[j]
			j += 1
		else:
			numbers[k] = left[i]
			i += 1
		k += 1
	# add remaining elements of the other list
	while i < len(left):
		numbers[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		numbers[k] = right[j]
		j += 1
		k += 1

main()