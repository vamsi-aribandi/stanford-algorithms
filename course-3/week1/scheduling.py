def main():
	jobs = []
	with open('test_jobs.txt') as f:
		next(f)
		jobName = 1
		for line in f:
			lineList = line.split(' ')
			jobs.append((jobName, int(lineList[0]), int(lineList[1])))
			jobName += 1
	factor = input("enter 'd' to schedule by difference(not optimal), 'r' for ratio(optimal): ")
	print(schedule(jobs, factor)[1])

def schedule(jobs, factor):
	"""
	schedule(jobs, factor):
	Function to schedule jobs based on ratio or difference or value and length.
	returns final schedule and weighted length of jobs
	"""
	if factor == 'r':
		jobs.sort(key = keyfn_ratio, reverse = True)
	elif factor == 'd':
		jobs.sort(key = keyfn_diff, reverse = True)
	else:
		return 'ERROR', 'ERROR'
	finalSchedule = []
	weightedLength, completedLength = 0, 0
	for job in jobs:
		completedLength += job[2]
		weightedLength += job[1] * completedLength
		finalSchedule.append(job[0])
	return finalSchedule, weightedLength

def keyfn_ratio(element):
	"""
	key fn to make sure jobs are sorted by ratio value/length, and settles ties by putting job with larger value first
	"""
	return element[1] / element[2], element[1]

def keyfn_diff(element):
	"""
	key fn to make sure jobs are sorted by difference value-length, and settles ties by putting job with larger value first
	"""
	return element[1] - element[2], element[1]

main()