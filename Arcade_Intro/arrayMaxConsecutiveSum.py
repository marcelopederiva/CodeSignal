def arrayMaxConsecutiveSum(a, k):    
    ant = sum(a[0:k])
    m =ant
    for i in range(0,len(a)-k):
        f = ant + a[k+i]-a[i]
        ant = f
        m = max(f,m)
    return(m)
