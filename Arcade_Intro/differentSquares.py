import numpy as np
def differentSquares(matrix):
    matrix = np.array(matrix)
    linha = len(matrix[:,0])
    coluna = len(matrix[0,:])
    mt=[]
    m=[]
    k=0
    c=0
    for i in range(linha-1):
        for j in range(coluna-1):
            m = matrix[i:i+2,j:j+2]
            m = m.tolist()
            if m not in mt:
                mt.append(m)
                c+=1
                m=[]

    return c