def RECLIS(arr):
    tmp = 1
    n = len(arr)
    for i in range(1,n):
        if arr[i] < arr[n-1]:
            comp = RECLIS(arr[:i+1]) + 1
            if  comp > tmp:
                tmp = comp
    return tmp

def DPLIS(arr):
    n = len(arr)
    lis = [1]*int(n)
    max = 1
    for j in range(0,n):
        for i in range(0, j):
            if arr[i] < arr[j]:
                if lis[i] + 1 > lis[j]:
                    lis[j] = lis[i] + 1
                    if lis[j] > max:    #instead of returni max(lis), we will just keep track of the max to avoid another n time operation to find the max.
                        max = lis[j]
    return max
    
def main():
    arr = [6,1,3,2,4,5,7,2,10]
    # print("REC LIS: " + str(RECLIS(arr)))
    print("DP LIS: " + str(DPLIS(arr)))
main()