def visit(v, graph, visited, finished=None):
	visited[v] = True
	for neighbor in graph[v]:
		if visited[neighbor] is not True:
			visit(neighbor, graph, visited, finished)
	finished.append(v)


def reverseTopo(graph):
	visited = {}
	finished = []
	for vertex in graph:
		visited[vertex] = False
	for vertex in graph:
		if visited[vertex] is not True:
			visit(vertex, graph, visited, finished) 
	return finished

"""def reversedGraph(graph):
	rGraph = {}
	for vertex in graph:
		for neighbor in graph[vertex]:
			if neighbor in rGraph:
				rGraph[neighbor].append(vertex)
			else:
				rGraph[neighbor] = [vertex]
	return rGraph
"""
def kosaraju(graph,rGraph):
	rTopo = reverseTopo(graph)
	#rGraph = reversedGraph(graph)
	
	SCCs = []
	visited = {}
	for vertex in rTopo:
		visited[vertex] = False

	while len(rTopo) > 0:
		current = rTopo.pop()
		if visited[current] is not True:
			scc = []
			visit(current, rGraph, visited, scc)
			SCCs.append(scc)

	return SCCs

#format --> (x, 1) == x && (x, 0) == not-x
def canSat(SCCs):
	for component in SCCs:
		truthValues = {}
		for vertex in component:
			if vertex[0] not in truthValues:
				truthValues[vertex[0]] = vertex[1]
			elif truthValues[vertex[0]] is not vertex[1]:
				return False
	return True

def inside(num, stretch):
	return num > stretch[0] and num < stretch[1]

def outside(num, stretch):
	return  num < stretch[0] or num > stretch[1]

def cross(x, y):
	return (outside(x[0], y) and inside(x[1],y)) or (inside(x[0],y) and outside(x[1],y))

def reduction(roads):
	temp = [int(i) for i in roads.strip().split(',')]		
	roads = zip(temp[::2], temp[1::2])
	graph = {}
	rGraph = {}

	for i in range(0, len(roads)):
		graph[(i,0)] = []
		graph[(i,1)] = []
		rGraph[(i,0)] = []
		rGraph[(i,1)] = []


	for i in range(0, len(roads)):
		for j in range(0, len(roads)):
			if i is j:
				continue
			if cross(roads[i], roads[j]):
				graph[(i,0)].append((j,1))
				graph[(i,1)].append((j,0))
				rGraph[(j,1)].append((i,0))
				rGraph[(j,0)].append((i,1))

	
	return graph,rGraph

def main():
	with open('input.txt') as infile:
		infile.readline()
		roads = infile.readline()

	graph,rGraph = reduction(roads)
	SCCs = kosaraju(graph,rGraph)
	result = "YES" if canSat(SCCs) else "NO"

	with open('output.txt', 'w') as outfile:
		outfile.write(result+'\n')
main()
