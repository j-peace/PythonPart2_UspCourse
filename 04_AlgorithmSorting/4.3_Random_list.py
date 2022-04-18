# This code receive an number and return a randon list with x elements.
import random

def lista_grande(n):
    rList = []
    for i in range(n):
        x = random.randint(1,3)
        rList.append(x)
    return rList

