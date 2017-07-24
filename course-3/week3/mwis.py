def main():
	with open('test_mwis.txt') as f:
		next(f) # skip first line, we will be appending anyway
		pathGraph = [None] # pathGraph[name] = value, so make pathGraph[0] = None since names start from 1
		for line in f:
			pathGraph.append(int(line))
	resultSet = generateSet(pathGraph)
	print(generate_string(resultSet, len(pathGraph) - 1))

def generateSet(pathGraph):
	"""
	Function to return a set of all vertices belonging to the max weighted independant set of pathGraph
	"""
	n = len(pathGraph) - 1
	solutions = [0, 0, 0]
	solutions[1] = pathGraph[1]
	solutions[2] = max(pathGraph[1], pathGraph[2])
	for vName in range(3, n + 1): # populate array of solutions to subproblems
		solutions.append(max(solutions[vName - 1], solutions[vName - 2] + pathGraph[vName]))
	# from solutions, construct set of vertices belonging to original problem of size n
	vSet = set()
	vName = n
	while vName > 0:
		if solutions[vName - 2] + pathGraph[vName] > solutions[vName - 1]:
			vSet.add(vName)
			vName -= 2
		else:
			vName -= 1
	return vSet

def generate_string(vSet, n):
	result = ''
	# for i in range(1, n + 1):
	for i in [1, 2, 3, 4, 17, 117, 517, 997]:
		if i in vSet:
			result += '1'
		else:
			result += '0'
	return result

main()