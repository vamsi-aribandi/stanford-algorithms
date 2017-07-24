import heapq

def main():
	vDict = {}
	eDict = {}
	with open('test_edges.txt') as f:
		next(f)
		edgeName = 1
		for line in f:
			tempList = line.split(' ')
			for vertex in tempList[0:2]:
				try:
					vDict[vertex].add(edgeName)
				except KeyError:
					vDict[vertex] = {edgeName}
			eDict[edgeName] = (tempList[0], tempList[1], int(tempList[2])) # vertex1, vertex2, cost
			edgeName += 1
	print(prim(vDict, eDict, '1'))

def prim(vDict, eDict, root):
	"""
	prim(vDict, eDict, root)
	Function to return cost of MST of an undirected graph using prim's algorithm.
	vDict[vertex] = [all edges of vertex]
	eDict[edge] = (vertex1, vertex2, cost)
	"""
	spanned = set()
	vertices = set(vDict)
	cost = 0
	vKeys = {}
	for vertex in vertices:
		vKeys[vertex] = 99999 # vKeys[vertex] = smallest distance to spanned vertices, MAX if no connection to spanned
	vKeys[root] = 0
	crossingEdgesHeap = []
	for vertex in vertices:
		heapq.heappush(crossingEdgesHeap, (vKeys[vertex], vertex)) # initialize heap of vertices
	while spanned != vertices:
		edgeCost, v = heapq.heappop(crossingEdgesHeap) # v is the vertex we are about to span
		cost += edgeCost
		spanned.add(v)
		# for all edges (v, w), where w has not been spanned
		for vEdge in vDict[v]:
			if eDict[vEdge][0] == v:
				w = eDict[vEdge][1]
			else:
				w = eDict[vEdge][0]
			if w not in spanned:
				vwCost = eDict[vEdge][2]
				for edge in crossingEdgesHeap:
					if edge[1] == w:
						crossingEdgesHeap.remove(edge) # messes up heap
						heapq.heapify(crossingEdgesHeap) # so we need to restore heap property
						break
				vKeys[w] = min(vwCost, vKeys[w])
				newEdge = (vKeys[w], w)
				heapq.heappush(crossingEdgesHeap, newEdge)
	return cost

main()