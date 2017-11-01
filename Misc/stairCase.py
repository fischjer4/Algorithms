def merge(left,right):
    l = 0
    r = 0
    max = []
    for i in range(0,len(left)+len(right)):
        print(max)
        if l >= len(left) and r < len(right):
            if right[r][1] < max[l-1][1] and right[r][0] > max[l-1][0]:
                max.append(right[r])
                r += 1
        elif r >= len(right) and l < len(left):
            if max[r-1][1] > left[l][1] and max[r-1][0] < left[l][0]:
                max.append(left[l])
                l += 1
        elif l < len(left) and r < len(right) and right[r][1] > left[l][1]:
            max.append(right[r])
            if left[l][0] > right[r][0]:
                max.append(left[l])
            r += 1
            l += 1            
        elif l < len(left) and r < len(right) and left[l][1] > right[r][1]:
            max.append(left[l])
            if right[r][0] > left[l][0]:
                max.append(right[r])       
            l += 1
            r += 1
    return max
def stairPoints(X):
    if len(X) <= 1:
        return X
    mid = len(X) // 2
    left = stairPoints(X[:mid])
    right = stairPoints(X[mid:])
    return merge(left, right)


def main():
    X = [(5,1),(1,2),(2,4),(7,0),(2,3),(1,5),(3,1),(4,2),(6,1)]
    d = stairPoints(X)
    print(d)
main()