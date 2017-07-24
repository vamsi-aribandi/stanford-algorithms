import heapq, sys

class node:
	def __init__(self, name = None, zeroNode = None, oneNode = None):
		self.name = name
		self.zeroNode = zeroNode
		self.oneNode = oneNode

def main():
	sys.setrecursionlimit(1010) # needed because input size is n = 1000, so we recurse 1000 times, which is above defualt recursion limit
	with open('test_huffman.txt') as f:
		next(f) # skip first line
		nHeap, cName = [], 1
		for line in f:
			heapq.heappush(nHeap, (int(line), str(cName)))
			cName += 1
	nDict = {} # a dict to store node objects by their names
	for x in nHeap:
		nDict[x[1]] = node(x[1]) # initialize dict with individual characters
	tree = makeTree(nHeap, nDict)
	cDict = {}
	makeEncoding(tree, cDict)
	print('max length: {}'.format(max(len(x) for x in cDict.values())))
	print('min length: {}'.format(min(len(x) for x in cDict.values())))

def makeTree(nHeap, nDict):
	"""
	makeTree(nHeap, nDict):
	Function to generate a tree of huffman codes,
	given a heap of tuples(weight, name) and a dict(to find nodes by name)
	"""
	aWeight, aName = heapq.heappop(nHeap)
	bWeight, bName = heapq.heappop(nHeap)
	abName = ','.join(aName.split(',') + bName.split(','))
	ab = node(abName, nDict[aName], nDict[bName])
	del nDict[aName], nDict[bName]
	if len(nHeap) == 0: # tree is made, no more nodes to add to it.
		return ab
	else:
		heapq.heappush(nHeap, (aWeight + bWeight, abName))
		nDict[abName] = ab
		return makeTree(nHeap, nDict)

def makeEncoding(tree, cDict, encoding = ''):
	"""
	makeEncoding(tree, cDict, encoding = ''):
	Function to populate cDict with the encodings of characters, given their huffman tree.
	"""
	if tree.zeroNode != None:
		makeEncoding(tree.zeroNode, cDict, encoding + '0')
	if tree.oneNode != None:
		makeEncoding(tree.oneNode, cDict, encoding + '1')
	if tree.zeroNode == None and tree.oneNode == None:
		cDict[tree.name] = encoding

main()