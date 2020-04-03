def digitDegree(n):
    c=0
    if n ==0:return c
    while n>9:
        m=0
        n = str(n)
        n = list(map(int,n))
        print(n,m)
        n = sum(n)    
        c +=1
    return c
