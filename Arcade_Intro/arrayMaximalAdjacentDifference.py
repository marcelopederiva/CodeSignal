def arrayMaximalAdjacentDifference(a):
    d = 0
    d2 = -1
    for i in range(0,len(a)-1):
            d = abs(a[i]-a[i+1])
            if d> d2:
                d2 = d
    return d2