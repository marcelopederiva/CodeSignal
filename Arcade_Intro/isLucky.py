def isLucky(n):
    p = len(list(str(n)))
    e = list(str(n))
    p1 = 0
    p2 = 0
    for i in range(0,int(p/2)):
        p1 = p1 + int(e[i])
        p2 = p2 + int(e[i+int(p/2)])
    return p1 == p2
    
