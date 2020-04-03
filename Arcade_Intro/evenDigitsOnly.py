def evenDigitsOnly(n):
    new = list(map(int,str(n)))
    
    for i in range(0,len(new)):
        if new[i]%2 != 0:
            return False
        
    return True
    