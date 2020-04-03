import numpy as np
def boxBlur(image):
    linha = np.shape(image)[0] -2
    coluna = np.shape(image)[1] -2
    i=0
    final =np.zeros((linha,coluna))
    sum =0
    for a in range(0,linha):
        for b in range(0,coluna):
            for p in range(a,a+3):
                for k in range(b,b+3):
                    sum = sum + image[p][k]            
            final[a][b] = int(sum/9)
            sum = 0
            
    return final