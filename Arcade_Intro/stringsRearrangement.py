from itertools import permutations

def stringsRearrangement(a):

    p=0
    v=[]
    for b in permutations(a):
        for i in range(1,len(b)):
            r = 0
            for j in range(len(b[0])):
                if b[i-1][j]!=b[i][j]:
                    r +=1
            if r !=1 :
                p=1
                v.append(False)
                
        if p==0:
            v.append(True)
        p=0
    return any(v)


    
    
    
    