def item( num ):
    if num == 0 :
        res = 0
    elif num == 1:
        res = 1
    else:
        res = item ( num - 1) + item (num -2)
    return res

def printFibo( no ):
    i = 0

    while i < no:
        print item(i)
        i += 1

printFibo(5)