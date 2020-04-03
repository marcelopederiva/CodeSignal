def sortByHeight(a):
    c = a.count(-1)
    b = sorted(a)
    p = 0
    for i in range(0,len(a)):
        if a[i]== -1:
            continue
                     
        else:
            
            a[i] = b[(c)+p]
            p+=1
    return a
  