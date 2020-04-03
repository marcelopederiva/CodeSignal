def alphabeticShift(inputString):
    new = list(map(str,str(inputString)))
    alf = 'abcdefghijklmnopqrstuvwxyz'
    alf = list(map(str,str(alf)))
    dic = 'bcdefghijklmnopqrstuvwxyza'
    
    dic = list(map(str,str(dic)))
    
    for i in range(0,len(new)):
        new[i] = dic[alf.index(new[i])]
        
    # separator  = ''.joint(new)   
    separator = ''.join(str(x) for x in new)
    return separator