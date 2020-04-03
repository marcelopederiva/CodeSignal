def isCryptSolution(crypt, solution):
    d ={}
    for i in solution:
        d[i[0]]=i[1]
    n=[]
    new =''
    for word in crypt:
        for c in word:
            new+=d[c]
        if new[0]=='0' and len(new)>1:
            return False
        n.append(new)
        new=''
    if int(n[0])+int(n[1])==int(n[2]):
        return True
    else:
        return False
