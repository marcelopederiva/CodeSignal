import numpy as np
def sudoku2(grid):
    g = np.array(grid)
    for i in range(len(g)):
        for j in range(1,10):
            if np.count_nonzero(g[i]==str(j))==2:
                return False
            if np.count_nonzero(g[:,i]==str(j))==2:
                return False
            
    for k in range(0,len(g)-2,3):
        for l in range(0,len(g)-2,3):
            n = g[k:k+3,l:l+3]
            for i in range(0,len(n)):
                for j in range(1,10):
                    if np.count_nonzero(n==str(j))==2:
                        return False
    return True