def extractEachKth(a, k):
    b = a.copy()
    t=[]  
    for p in range(1,int(len(a)/k)+1):
            t.append(p*k-1)   
    for i in range(0,len(t)): 
        b.remove(a[t[i]])
    return b
