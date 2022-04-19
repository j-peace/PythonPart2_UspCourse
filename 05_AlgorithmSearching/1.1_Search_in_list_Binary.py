# This code receive a number and search in a binary form where is this number.

def busca(lista, elemento):
    first = 0
    last = len(lista)-1

    while (first <= last):
        mid = (first+last)//2
        position = False
        print(mid)
        if lista[mid]==elemento:
            position = mid
            first = mid + 12
        else:
            if elemento < lista[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return position
