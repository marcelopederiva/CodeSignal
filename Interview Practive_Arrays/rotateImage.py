def rotateImage(a):
    p=[]
    r=[]
    for j in range(0,len(a)):
        for i in range(len(a)-1,-1,-1):
            p.append(a[i][j])
        r.append(p)
        p=[]
    return r