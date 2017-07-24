import random, copy

def main():
	vDict = {}
	with open('test.txt') as f:
		for line in f: # undirected graph file is such that per line, first no. is the vertex connected to all the other no.s(vertices) following it
			templist = line.split(' ') # for actual graph use .split('\t'), for test use .split(' ')
			vDict[int(templist[0])] = [int(x) for x in templist[1:-1]] # exclude last element, which is ''(empty string)
	min = len(vDict)
	for i in range(len(vDict)):
		cut = generate_cut(vDict)
		if cut < min:
			min = cut
	print(min)

def generate_cut(vDict):
	"""
	generate_cut(vDict):
	Function to return a number of cuts in vDict(vDict[vertex] = list of vertices connected to it)
	it contracts vertices until only two are left, and return the number of edges between them
	"""
	vDictCopy = copy.deepcopy(vDict)
	while len(vDictCopy) > 2:
		v1, v2 = choose_random_edge(vDictCopy)
		contract(vDictCopy, v1, v2)
	return len(list(vDictCopy.values())[0])

def choose_random_edge(vDict):
	"""
	choose_random_edge(vDict):
	Function to return two random connected vertices in a graph
	"""
	v1 = random.choice(tuple(vDict))
	v2 = random.choice(vDict[v1])
	return v1, v2

def contract(vDict, v1, v2):
	"""
	contract(vDict, v1, v2):
	Function to contract v2 to v1, deleting v2 from graph.
	"""
	for vertex in vDict[v2]:
		vDict[vertex].append(v1) # add v1 to all vertices connected to v2
		vDict[vertex] = [x for x in vDict[vertex] if x!= v2] # remove v2 from all vertices that were previously connected to v2
	vDict[v1] += vDict[v2] # connect all edges previously connected to v2 to v1
	vDict[v1] = [x for x in vDict[v1] if x != v1] # remove self loops
	del vDict[v2]

main()