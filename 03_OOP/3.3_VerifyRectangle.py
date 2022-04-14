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

    # Rectangle method
    def retangulo(self):
        h = self.a
        cat1, cat2 = self.b, self.c
        if(self.b > self.a and self.b > self.c):
            h = self.b
            cat1, cat2 = self.a, self.c
        else:
            if(self.c > self.b and self.c > self.a):
                h = self.c
                cat1, cat2 = self.a, self.b
        rectangle = False
        if (h**2 == cat1**2 + cat2**2):
            rectangle = True

        return rectangle

t = Triangulo(1, 3, 5)
print(t.retangulo())
# deve devolver False

u = Triangulo(3, 4, 5)
print(u.retangulo())
# deve devolver True