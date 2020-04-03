def palindromeRearranging(a):
    c=0
    for i in range(0,len(a)):
        print(len(a))
        if len(a)%2 != 0:
            if a.count(a[i]) == 1:
                c+=1
            if c>1:
                return False
        if len(a)%2==0:
            if a.count(a[i])%2!=0:
                return False            
    return True
