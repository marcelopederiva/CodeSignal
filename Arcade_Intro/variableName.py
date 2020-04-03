def variableName(name):
    new = list(map(str,str(name)))
    dic = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
    dic = list(map(str,str(dic)))
    try:
        b = int(new[0])
        return False
    except ValueError:
        print ('hey')
        for i in range(0,len(new)):
            if new[i] in dic:
                continue
            else:
                return False
        return True
        