def arrayChange(a):
    count = 0
    for i in range(0,len(a)-1):
        while a[i+1]<=a[i]: 
            count +=a[i]-a[i+1]+1
            a[i+1]= a[i]+1            
    return count