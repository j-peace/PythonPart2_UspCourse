# This code receive a matrice and print this line for line
def imprime_matriz(minha_matriz): 
    num_linhas = len(minha_matriz)
    num_colunas = len(minha_matriz[0])
    j = 0
    i = 0
    for i in range(num_linhas):
        linha = minha_matriz[i]
        for j in range(num_colunas):
            print(linha[j], end="")
        print("")

    pass 

minha_matriz = [[1, 2], [3, 4]]

imprime_matriz(minha_matriz)