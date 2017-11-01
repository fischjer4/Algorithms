###########################################################
#	Austin Row
#	Jeremy Fischer
#	10/11/2016
###########################################################
import math

def betweenIntersects(lines, startpoint, endpoint, midpoint):
	intersections = 0
	leftIter = startpoint
	rightIter = midpoint
	merged = list()

	while leftIter < midpoint:
		if rightIter < endpoint and lines[rightIter][1] <= lines[leftIter][1]:
			intersections = intersections + midpoint - leftIter
			merged.append((lines[rightIter][0], lines[rightIter][1]))
			rightIter = rightIter + 1
		else:
			merged.append((lines[leftIter][0], lines[leftIter][1]))
			leftIter = leftIter + 1

	for i in range(startpoint, len(merged)+startpoint):
		lines[i] = merged[i-startpoint]
	
	return intersections


def intersections(lines, startpoint, endpoint):
	if endpoint - startpoint <= 1:
		return 0
	
	midpoint = int(math.ceil((startpoint+endpoint)/2))
	
	numLeft = intersections(lines, startpoint, midpoint)
	numRight = intersections(lines, midpoint, endpoint)
	
	return numLeft+numRight+betweenIntersects(lines,startpoint,endpoint,midpoint)

def main():
	inputFile = open('input.txt','r')
	numLines = int(inputFile.readline())
	pSet = [int(x) for x in inputFile.readline().split(',')]
	qSet = [int(x) for x in inputFile.readline().split(',')]
	lines = [(pSet[i],qSet[i]) for i in range(0,numLines)]
	inputFile.close()
	outputFile = open('output.txt','w')
	outputFile.write(str(intersections(lines, 0, len(lines))))
	outputFile.close()
main()
