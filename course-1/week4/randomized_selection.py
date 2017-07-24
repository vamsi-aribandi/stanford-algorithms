import random

def main():
	numbers = [3,2,4,7,6,5,1,8]
	stat_order = 7
	print("array: {}".format(numbers))
	print("element of order {}: {}".format(stat_order, rand_select(numbers, 0, len(numbers) - 1, stat_order)))

def rand_select(list, left, right, order):
	"""
	rand_select(list, left, right, order):
	Function to return the "order"th smallest number in list
	"""
	old_pivot_index = random.randint(left, right)
	new_pivot_index = partition(list, left, right, old_pivot_index)
	if new_pivot_index == order - 1:
		return list[new_pivot_index]
	elif new_pivot_index > order - 1:
		return rand_select(list, left, new_pivot_index - 1, order)
	else:
		return rand_select(list, new_pivot_index + 1, right, order)

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

main()