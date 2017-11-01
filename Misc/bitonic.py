def bitonic(X,n):
    flag = 1
    counter = 1
    biggest = 1
    for i in range(n-1,0,-1):
        if(X[i - 1] > X[i]):
            if flag == 1:
                counter = counter + 1
            else:
                counter = 2
        else:
            if flag == 1:
                counter = counter + 1
                flag = 0
            else:
                counter = counter + 1
        if counter > biggest:
                    biggest = counter
    return biggest

def main():
	X = [3,1,2,3,2,1,4,5,9,7]
	print(bitonic(X,len(X)))

main()