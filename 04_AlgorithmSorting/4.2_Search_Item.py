# This code receive an element and return where it is.

from xml.etree.ElementTree import ElementTree


def busca(lista, elemento):
    position = False 
    for i in range (len(lista)):
        if (lista[i] == elemento): 
            position = i
    
    return position                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

print(busca([1, 5, 9, 5, "a", 6],  "a"))
