
def makeMatrix(rows, cols):
    return [[0 for x in range(rows)] for y in range(cols)] 


def findVertex(v,G,visited,stack):
    if visited[v] == 0:
        visited[v] = 1
        for e in range(0,len(G)):
            if G[v][e] == 1:
                findVertex(G[v][e],G,visited,stack)
        stack.append(v+1)
                
def TopoSort(G,visited,stack):
    sorted = []
    for v in range(0,len(G)):
        findVertex(v,G,visited,stack)
    return stack

def main():
    stack = []
    visited = [0]*8
    G = makeMatrix(8,8)
    G[0][2] = 1
    G[1][2] = 1
    G[1][3] = 1
    G[2][4] = 1
    G[3][5] = 1
    G[4][5] = 1
    G[4][7] = 1
    G[5][6] = 1

    GSorted = TopoSort(G,visited,stack)
    for i in GSorted:
        print(chr(i+64)),
    print('')
main()