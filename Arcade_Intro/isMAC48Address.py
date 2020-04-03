def isMAC48Address(a):
    h1 = 'ABCDEF0123456789'
    h1 = list(h1)
    a = list(a)  
    if len(a)!= 17:
        return False
    while a.count('-')!=0:
        a.remove('-')
    if len(a)!=12:
        return False
    for i in a:
        if i not in h1:
            return False
    return True
    
    
    
