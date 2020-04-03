import numpy as np
def minesweeper(matrix):
    linha = np.shape(matrix)[0] 
    coluna = np.shape(matrix)[1] 
    big = np.zeros((linha+2,coluna+2))
    m =np.zeros((linha,coluna))
    matrix = np.array(matrix)
    
    big[1:np.shape(big)[0]-1, 1:np.shape(big)[1]-1]=matrix
    for i in range(0,linha):
        for j in range(0,coluna):
            m[i][j]=(big[i:i+3,j:j+3]==True).sum()
            if matrix[i,j] == True:
                m[i][j] = m[i][j] -1
    # print((big[2:5,0:3]==True).sum(), print(big[2:5,0:3]))
    
    print(big)
           
    return m
