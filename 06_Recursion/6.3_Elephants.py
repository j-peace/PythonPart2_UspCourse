# This code receive a number and make the elephants music letter with the recursive form.

def incomodam(n):
    if n < 1:
        return ""
    else:
        return "incomodam " + incomodam(n - 1)

def elefantes(n):
    if n < 1:
        return ""
    if n == 1:
        return "Um elefante incomoda muita gente\n"
    else:
        return elefantes(n-1) + str(n) + " elefantes " + incomodam(n) +  " muito mais\n" + str(n + 1) + " elefantes incomodam muita gente\n"

print(elefantes(5))