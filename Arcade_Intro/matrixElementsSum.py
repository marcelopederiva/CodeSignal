import numpy as np
def matrixElementsSum(matrix):
    soma = 0
    c = len(matrix[0][:])-1
    l = len(matrix[:])-1
    print(c,l)
    
    
    for c in range(0,len(matrix[0][:])):
        for l in range(0,len(matrix[:])-1):
            if matrix[l][c]==0:
                matrix[l+1][c] = 0          
    

    print(matrix)
    m = np.array(matrix)
    return sum(sum(m))
    

#     # coluna
#     print (len(matrix[0][:]))
# #     linha
#     print(len(matrix[:]))
#     m[coluna][linha]