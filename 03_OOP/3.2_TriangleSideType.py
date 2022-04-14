# This code receive thre values that correspond the sides size of the triangle.

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c

    # This a new method 
    def tipo_lado(self):
        o = "escaleno"
        if (self.a == self.b and self.a == self.c):
            o = "equilátero"
        else:
            if (self.a == self.b or self.a == self.c or self.b == self.c):
                o = "isósceles"

        return o

t = Triangulo(3, 3, 3)
x = t.tipo_lado()

print(x)