# This code receive thre values that correspond the sides size of the triangle.

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c


t = Triangulo(13, 3, 3)

x = t.perimetro()

y = t.a

print(x, y)



# import pytest

# @pytest.mark.parametrize("input", "outputWanted",[
#     ([1, 1, 1], 3),
#     ([1, 1, 2], 4),
#     ([1, 1, 3], 5),
# ]
# )

