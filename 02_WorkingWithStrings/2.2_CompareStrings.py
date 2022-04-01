# This code receive a list of names and return the shorter name.

def menor_nome(nomes):
    i = 1
    b = nomes[0]
    for i in range(len(nomes) - 1):
        x = nomes[i]
        if (len(x.strip()) < len(b.strip())):
            b = x.strip()
                    
    return b.capitalize()

print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))