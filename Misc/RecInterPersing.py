        # if str1Count < len(str1):
        #     print('str1: ' + str(str1[str1Count]))
        # if str2Count < len(str2):
        #     print('str2: ' + str(str2[str2Count]))
        # if y < len(strComb):
        #     print('strComb: ' + str(strComb[y])) 
        # print("----------------------------------------------------------") 
def inter(str1Count, str2Count,y,str1, str2, strComb):
    if y >= len(strComb):
        return True
    if (str1Count < len(str1) and strComb[y] == str1[str1Count]) and (str2Count < len(str2) and strComb[y] == str2[str2Count]):
        wit = inter(str1Count + 1, str2Count,y + 1,str1, str2, strComb)
        if wit == False:
            without = inter(str1Count, str2Count + 1,y + 1,str1, str2, strComb)
            if without == False:
                return False
            else:
                return True
    if str1Count < len(str1) and strComb[y] == str1[str1Count]:
        return inter(str1Count + 1, str2Count,y + 1,str1, str2, strComb)
    elif str2Count < len(str2) and strComb[y] == str2[str2Count] :
        return inter(str1Count, str2Count + 1,y + 1,str1, str2, strComb)
    else:
        return False

def main():
    str1 = 'BADDDDDE'
    str2 = 'LADDDDDA'
    strComb = 'BALADDDDDDEDDDDA'
    isIt = inter(0,0,0,str1,str2,strComb)
    print(isIt)
main()