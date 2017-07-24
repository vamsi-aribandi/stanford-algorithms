def main():
	numbers = []
	with open("test.txt") as f:
		for line in f:
			numbers.append(int(line))
	print("no. of inversions: {}".format(count_and_sort(numbers)))

def count_and_sort(numbers):
	"""
	count_and_sort(numbers):
	Function to count no. of inversions in a list as well as sort it.
	"""
	if len(numbers) > 1:
		mid = len(numbers) // 2
		left = numbers[:mid]
		right = numbers[mid:]
		count = count_and_sort(left)
		count += count_and_sort(right)
		count += merge_and_count_split(left, right, numbers)
		return count
	else:
		return 0

def merge_and_count_split(left, right, numbers):
	"""
	merge_and_count_split(left, right, numbers):
	Function to count the number of split inversions of a list, given both halves.
	It is just the merge subroutine from mergesort with a small addition
	"""
	i, j, k, count = 0, 0, 0, 0
	while i < len(left) and j < len(right):
		if left[i] > right[j]:
			numbers[k] = right[j]
			count += len(left) - i # count all split inversions in `numbers` containing right[j] (i.e. no. of items to right of left[i])
			j += 1
		else:
			numbers[k] = left[i]
			i += 1
		k += 1
	while i < len(left):
		numbers[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		numbers[k] = right[j]
		j += 1
		k += 1
	return count

main()