# This code receive a sentence and return only the uppercase letters.

def maiusculas(frase): 
    capitalLetters = ""
    i = 0
    for i in range(len(frase)):
        if (ord(frase[i]) > 64 and ord(frase[i]) < 91):
            capitalLetters += frase[i]
                    
    return capitalLetters

print(maiusculas('PrOgRaMaMoS em python!'))

# Uppercase
# >64 and <91 

# Lowercase
# >96 and <123