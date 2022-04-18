# This code receive a list and test if the values are ordered.

def ordenada(lista):
    ordered = True
    for i in range (len(lista)-1):
        if (lista[i + 1] < lista[i]): 
            ordered = False
    
    return ordered

print(ordenada([1, 5, 5, 6]))
