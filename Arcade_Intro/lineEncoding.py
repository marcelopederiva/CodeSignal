def lineEncoding(s):
    s = list(s)
    s.append('0')
    c=1
    n=[]
    for i in range(0,len(s)-1):
        if s[i+1] == s[i]:
            c = c+1

        else:
            if c!=1:
                n.append(c)
            c=1
            n.append(s[i])
    for j in range(len(n)):
        n[j] = str(n[j])
    return ''.join(n)       
