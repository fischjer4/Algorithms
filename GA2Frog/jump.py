from math import pow
from math import sqrt
from math import ceil
import re

def distance(point1, point2):
	return int(ceil(sqrt(pow(point2[0]-point1[0] , 2) + pow(point2[1]-point1[1] , 2))))

def jump(P, Q, L):
	Cache = [[False for i in range(0,len(Q))] for j in range(0,len(P))]
	if distance(P[0], Q[0]) <= L:
		Cache[0][0] = True
	else:
		return False

	for i in range(1, len(P)):
		Cache[i][0] = False if distance(P[i],Q[0]) > L or not Cache[i-1][0] else True

	for i in range(1, len(Q)):
		Cache[0][i] = False if distance(P[0],Q[i]) > L or not Cache[0][i-1] else True 
	
	for i in range(1, len(P)):
		for j in range(1, len(Q)):
			if distance(P[i], Q[j]) <= L and (Cache[i-1][j] or Cache[i][j-1] or Cache[i-1][j-1]):
				Cache[i][j] = True
			else:
				Cache[i][j] = False
	
	return Cache[-1][-1]

def main():
	inputFile = open("./input.txt","r")
	inputFile.readline()
	P = re.findall('(-?\d+,-?\d+)',inputFile.readline())
	P = [(int(y[0]), int(y[1])) for y in (x.split(',') for x in P)]
	inputFile.readline()
	Q = re.findall('(-?\d+,-?\d+)',inputFile.readline())
	Q = [(int(y[0]), int(y[1])) for y in (x.split(',') for x in Q)]
	inputFile.readline()
	L = [int(length) for length in inputFile.readline().split(',')]
	inputFile.close()
	L = sorted(L)	
	
	for i in xrange(0, len(L)):
		if jump(P, Q, L[i]):
			outputFile = open("output.txt","w")
			outputFile.write(str(L[i])+"\n")
			outputFile.close()
			break
main()
