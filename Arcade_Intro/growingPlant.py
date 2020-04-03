def growingPlant(up, down, desiredHeight):
    h = 0
    c=0
    while h <=desiredHeight:
        h += up
        if h >=desiredHeight:
            return c+1
        h -= down
        c +=1
        
    return c
