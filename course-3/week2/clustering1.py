def main():
	vDict = {}
	eDict = {}
	with open('test_clustering1.txt') as f:
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
	result = cluster(vDict, eDict, 4)
	print(eDict[result])

def clusterTogether(v1, v2, clusterVertexDict, vertexClusterDict):
	"""
	clusterTogether(v1, v2, clusterVertexDict, vertexClusterDict):
	Function to cluster vertices v1 and v2 together.
	"""
	if vertexClusterDict[v1] != vertexClusterDict[v2]: # if vertices aren't in same cluster
		# check which cluster is smaller/bigger among the two:
		if len(clusterVertexDict[vertexClusterDict[v1]]) < len(clusterVertexDict[vertexClusterDict[v2]]):
			smallCluster = vertexClusterDict[v1]
			bigCluster = vertexClusterDict[v2]
		else:
			smallCluster = vertexClusterDict[v2]
			bigCluster = vertexClusterDict[v1]
		# combine clusters of v1 and v2:
		for vertex in clusterVertexDict[smallCluster]:
			vertexClusterDict[vertex] = bigCluster
		clusterVertexDict[bigCluster] = clusterVertexDict[bigCluster] | clusterVertexDict[smallCluster]
		del clusterVertexDict[smallCluster]

def cluster(vDict, eDict, n):
	"""
	cluster(vDict, eDict, n):
	Function to find the "best" clustering, with n of clusters.
	It returns the smallest edge crossing between any two clusters, a measure for how "good" the clustering is.
	"""
	sortedEdges = sorted(list(eDict), key = lambda x: eDict[x][2]) # sort edges by cost
	clusterVertexDict, vertexClusterDict = {}, {}
	for vertex in vDict: # initialize dicts of vertices pointing to their clusters and vice-versa
		vertexClusterDict[vertex] = vertex
		clusterVertexDict[vertex] = {vertex}
	i = 0
	while len(clusterVertexDict) > n: # main loop
		edge = sortedEdges[i]
		v1, v2, edgeLen = eDict[edge]
		clusterTogether(v1, v2, clusterVertexDict, vertexClusterDict)
		i += 1
	# after clustering, we must now find the next smallest edge crossing between clusters
	edge = sortedEdges[i]
	v1, v2, edgeLen = eDict[edge]
	while vertexClusterDict[v1] == vertexClusterDict[v2]:
		edge = sortedEdges[i]
		v1, v2, edgeLen = eDict[edge]
		i += 1
	return sortedEdges[i - 1]

main()