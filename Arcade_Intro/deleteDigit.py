def deleteDigit(n):
    n = str(n)
    nb =[]
    cpy = n
    for i in range(len(n)):
        nb.append(cpy[:i]+cpy[(i+1):])
    nb = list(map(int,nb))
    print(nb)
    return max(nb)
