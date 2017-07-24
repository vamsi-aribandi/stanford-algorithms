def main():
	vDict = {}
	with open('test.txt') as f:
		for line in f:
			tempList = line.split('\t')
			vDict[int(tempList[0])] = []
			for v in tempList[1:]: # use [1:-1] for actual graph, [1:] for test
				tempstr = v.split(',')
				vDict[int(tempList[0])].append((int(tempstr[0]), int(tempstr[1])))
	start = int(input('enter start vertex: '))
	end = int(input('enter end vertex: '))
	print('shortest path length = {}'.format(dijkstra(vDict, start, end)))

def dijkstra(vDict, start, end):
	"""
	dijkstra(vDict, start, end):
	Function to return shortest path length from start to end vertices using dijkstra's algorithm,
	Given directed, weighted graph vDict = {all v: [all (u, weight) for u connected to v]}.
	"""
	dist = {start: 0, 'INITIAL': 9999999999}
	seen = {start}
	while(end not in seen):
		mintail = 'INITIAL'
		minweight = dist[mintail]
		for tail in seen:
			for head, weight in vDict[tail]:
				if head not in seen and weight + dist[tail] < minweight + dist[mintail]:
					minweight = weight
					mintail = tail
					minhead = head
		if minweight == 9999999999:
			return 'NO PATH FOUND'
		dist[minhead] = minweight + dist[mintail]
		seen.add(minhead)
	return dist[end]

main()