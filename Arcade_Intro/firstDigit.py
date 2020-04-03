def firstDigit(a):
    a = list(a)
    for i in range(len(a)):
        try:
            b = int(a[i])
            return str(b)    
        except ValueError:
            continue
