# This code receive a list and return the recursive list with odd algarims.

def encontra_impares(lista):
    if not lista:
        return []
    if lista[0]%2 == 1:
        return [lista[0]] + encontra_impares(lista[1:])
    return encontra_impares(lista[1:])

print(encontra_impares([2,2,5,10,10,7,10,3,4]))