from collections import deque

def main():
	start = int(input('enter start vertex: '))
	end = int(input('enter end vertex: '))
	vDict = {}
	with open('test.txt') as f:
		for line in f:
			tempList = line.split(' ')
			try:
				vDict[int(tempList[0])].append(int(tempList[1]))
			except KeyError:
				vDict[int(tempList[0])] = [int(tempList[1])]
	print('shortest path length = {}'.format(shortest_path_length(vDict, start, end)))

def shortest_path_length(vDict, start, end):
	"""
	shortest_path_length(vDict, start, end):
	Function to return the shortest path length between start and end vertices,
	It uses BFS to do so.
	"""
	queue = deque([start])
	seen = {start}
	dist = {start: 0}
	while end not in seen:
		u = queue.popleft()
		for v in vDict[u]:
			if v not in seen:
				dist[v] = dist[u] + 1
				queue.append(v)
				seen.add(v)
	return dist[end]

main()