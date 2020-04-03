def alternatingSums(a):
    b = []
    c = []
    d = []
    for i in range(0,len(a)): 
        if i%2 == 0:
            b.append(a[i])
        elif i%2!=0:
            c.append(a[i])
    d.append(sum(b))
    d.append(sum(c))
    return d

