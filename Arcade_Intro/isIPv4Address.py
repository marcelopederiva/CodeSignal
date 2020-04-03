def isIPv4Address(a):
    a = a.split('.')
    a2 =[]
    if len(a)!=4:
        return False
    try:
        for i in range(0,len(a)):
            a2.append(int(a[i]))
            print(a2)
            if a2[i]<0 or a2[i]>255:
                return False 
        return True
            
    except ValueError:
        return False
