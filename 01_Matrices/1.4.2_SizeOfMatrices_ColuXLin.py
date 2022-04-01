# This code receive two matrices and return true if these have the same size
from operator import truediv

def sao_multiplicaveis(m1, m2): 
    matriz = False
    fatalError = True
    i = 0
    for i in range(len(m1)):
        if (len(m1) == len(m2[i])):
            matriz = True
        else:
            fatalError = False
    if fatalError == False:
        matriz = False
                    
    return matriz

m1 = [[1, 2, 3], [4, 5, 6], [4, 5, 6], [4, 6]]
m2 = [[2, 3, 4], [5, 6, 7], [4, 5, 6], [4, 5, 6]]

sao_multiplicaveis(m1, m2)