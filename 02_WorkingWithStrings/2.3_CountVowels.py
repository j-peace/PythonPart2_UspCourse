# This code receive a sentence and a parameter and return the number of vowels or consonants.

def conta_letras(frase, contar="vogais"):
    sentence = frase.replace(" ", "")
    vow, h = 0, len(sentence)
    x = len(frase.replace(" ", ""))
    for i in range(len(sentence)):
        if (sentence[i] == "a" or sentence[i] == "e" or sentence[i] == "i" or sentence[i] == "o" or sentence[i] == "u"):
            vow += 1

    if (contar == "consoantes"):
        result = len(frase.replace(" ", "")) - vow
    else:
        result = vow

    return result

print(conta_letras('programamos em python', 'consoantes'))