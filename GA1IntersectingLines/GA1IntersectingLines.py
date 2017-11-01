def err(errStr):
    print(errStr)
    exit()

def parsePoints(pointStr):
    nlStriped = pointStr.rstrip() #strips newline
    points = nlStriped.split(',') 
    for i in range(0,len(points)):
        points[i] = int(points[i]) #turn str into int
    return points

def merge(curList,m):

def mergeSort(qPoints):
    if len(qPoints) > 1:
        m = (len(qPoints) / 2)
        mergeSort(qPoints[:m])
        mergeSort(qPoints[m+1:])
        merge(qPoints,m)

def findInters(counter, itr, qPoints):
    mergeSort(qPoints)
    print(qPoints)

def findInters(counter, itr, qPoints):
    if itr > 0:
        counter = findInters(counter, itr - 1, qPoints)
    for i in range(0,itr):
        if(qPoints[itr] < qPoints[i]):
            counter = counter + 1
    return counter

def main():
    try:
        fileInput = open('input.txt','r')
    except:
        err('NO input.txt provided')
    if(fileInput):
        try:
            numPoints = int(fileInput.readline())
            pPoints = parsePoints(fileInput.readline()) #returns a list of integers representing points
            qPoints = parsePoints(fileInput.readline())
        except:
            err('Unable to parse input.txt')
        fileInput.close()

        counter = findInters(0, numPoints -1, qPoints)
        # fileOutput = open('output.txt','w')
        # fileOutput.truncate()
        # fileOutput.write(str(counter))
        # fileOutput.close()
    else:
        err('No input.txt')

main()