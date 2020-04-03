def allLongestStrings(inputArray):
    c = []
    n =[]
    for i in range(0,len(inputArray)):
        c.append(len(list(inputArray[i])))
    for i in range(0,len(inputArray)):
        if c[i] == max(c):
            n.append(inputArray[i])
    return n
