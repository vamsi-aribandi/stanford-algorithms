import heapq

def main():
	vDict, vDictRev = {}, {}
	with open('test.txt') as f:
		for line in f:
			tempList = line.split(' ')
			try:
				vDict[int(tempList[0])].append(int(tempList[1]))
			except KeyError:
				vDict[int(tempList[0])] = [int(tempList[1])]
			try:
				vDictRev[int(tempList[1])].append(int(tempList[0]))
			except KeyError:
				vDictRev[int(tempList[1])] = [int(tempList[0])]
	print(kosaraju_two_pass(vDict, vDictRev))

def kosaraju_two_pass(vDict, vDictRev):
	vList = list(set(vDictRev) | set(vDict))
	seen = set()
	finishTimes = {'time': 0}
	components = {'current component': vList[0]}
	for v in vList:
		if v not in seen:
			dfs_loop(vDictRev, v, seen, finishTimes, components)
	vList.sort(key = lambda x: finishTimes[x], reverse = True)
	components = {'current component': vList[0]}
	seen = set()
	for v in vList:
		if v not in seen:
			components['current component'] = v
			dfs_loop(vDict, v, seen, finishTimes, components)
	del components['current component']
	return heapq.nlargest(5, [len(x) for x in components.values()])

def dfs_loop(vDict, start, seen, finishTimes, components):
	seen.add(start)
	stack = [start, start]
	while len(stack) > 0:
		u = stack.pop()
		if u not in stack:
			finishTimes['time'] += 1
			finishTimes[u] = finishTimes['time']
		try:
			components[components['current component']].add(u)
		except KeyError:
			components[components['current component']] = {u}
		try:
			for v in vDict[u]:
				if v not in seen:
					stack.append(v)
					stack.append(v)
					seen.add(v)
		except KeyError:
			pass

def dfs_rec(vDict, start, seen, finishTimes, components):
	seen.add(start)
	try:
		components[components['current component']].add(start)
	except KeyError:
		components[components['current component']] = {start}
	try:
		for v in vDict[start]:
			if v not in seen:
				dfs_rec(vDict, v, seen, finishTimes, components)
	except KeyError:
		pass
	finishTimes['time'] += 1
	finishTimes[start] = finishTimes['time']

main()