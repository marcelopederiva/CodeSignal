def longestDigitsPrefix(a):
    a = list(a)
    b=[]
    for i in range(len(a)):
        try:
            b.append(int(a[i]))
        except ValueError:
            break
    b = ''.join(str(x) for x in b)
    return b
