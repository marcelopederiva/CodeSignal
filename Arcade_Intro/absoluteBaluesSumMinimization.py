def absoluteValuesSumMinimization(a):
    x =[]
    s = 0
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            s = s + abs(a[i] - a[j]) 
        x.append(s)
        s = 0
    return a[x.index(min(x))]   
