def isBeautifulString(a):
    dic = 'abcdefghijklmnopqrstuvwxyz'
    dic= list(dic)
    l=[]
    for i in range(len(dic)):
        c = a.count(dic[i])
        l.append(c)
    print(l)
    for j in range(len(l)-1):
        if l[j+1]>l[j]:
            return False
    return True