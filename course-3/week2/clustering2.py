def main():
	vertices = []
	with open('test_clustering2.txt') as f:
		next(f)
		vName = 1
		for line in f:
			tempString = str(line)[:-1]
			vertices.append(tempString.replace(' ', ''))
	print(cluster(vertices))

def cluster(vList):
	"""
	cluster(vList):
	Function to cluster all vertices of distance 1 or 2 from each other together.
	It returns the maximum number of clusters required to do so.
	"""
	vertexClusterDict = {}
	clusterVertexDict = {}
	for vertex in vList:
		vertexClusterDict[vertex] = vertex
		clusterVertexDict[vertex] = {vertex}
	for vertex in vList:
		for x in generateList(vertex):
			if x in vertexClusterDict:
				clusterTogether(vertex, x, clusterVertexDict, vertexClusterDict)
	return len(clusterVertexDict)

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

def generateList(s):
	"""
	generateList(s):
	Function to make a list of all vertices(strings) at a distance of 1 or 2 from s
	"""
	sLen = len(s)
	result = []
	# loop to append all variations of s with only one character inverted
	for i in range(sLen):
		temp = list(s)
		if temp[i] == '0':
			temp[i] = '1'
		else:
			temp[i] = '0'
		result.append(''.join(temp))
	# loop to append all variations of s with only two characters inverted
	for i in range(sLen):
		for j in range(i + 1, sLen):
			temp = list(s)
			for x in (i, j):
				if temp[x] == '0':
					temp[x] = '1'
				else:
					temp[x] = '0'
			result.append(''.join(temp))
	return result

main()