def areSimilar(a, b):
    if a==b:
        return True
    c=[]
    bad_count=0
    for y in range(len(a)):
        if a[y]!=b[y]:
            c+=[y]
        if len(c)>2:
            return False    
    if len(c)==0:
        return True
    elif len(c)==2 and a[c[1]]==b[c[0]] and a[c[0]]==b[c[1]]:
        return True
    else:
        return False