def soma_matrizes(m1, m2): 
    matriz = False
    if (len(m1) == len(m2)):
        num_linhas = len(m1)
        num_colunas = len(m1[0])
        j = 0
        i = 0
        matriz = []  #lista vazia
        for i in range(num_linhas):
            linha1 = m1[i]
            linha2 = m2[i]
            linhaTot = []
            for j in range(num_colunas):
                valor = linha1[j] + linha2[j]
                linhaTot.append(valor)
            matriz.append(linhaTot)

    return matriz

m1 = [[1, 2, 3], [4, 5, 6], [4, 5, 6], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7], [4, 5, 6], [4, 5, 6]]

soma_matrizes(m1, m2)