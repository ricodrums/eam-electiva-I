
class ComplexNumber:

    @property
    def module(self):
        return (self.a * self.a + self.b * self.b) ** (1/2)

    def __init__(self, a = 0, b = 0) -> None:
        self.a = a
        self.b = b

    def __add__(self, complex):
        return ComplexNumber(self.a + complex.a, self.b + complex.b)

    def __sub__(self, complex):
        return ComplexNumber(self.a - complex.a, self.b - complex.b)

    def __mul__(self, complex):
        c = self.a * complex.a - self.b * complex.b
        d = self.a * complex.b + self.b * complex.a
        return ComplexNumber(c, d)


    def __truediv__(self, complex):
        if complex.module == 0:
            return
        else:
            c = (self.a * complex.a + self.b * complex.b) / complex.module * complex.module
            d = (self.b * complex.a - self.a * complex.b) / complex.module * complex.module
            return ComplexNumber(c, d)
            
    def __eq__(self, complex: object) -> bool:
        return self.a == complex.a and self.b == complex.b

    def __str__(self) -> str:
        if self.a == 0 and self.b == 0:
            return '0'
        if self.b > 0:
            return f'{self.a}+{self.b}i'
        return f'{self.a}{self.b}i'

    @staticmethod
    def is_pure(complex):
        if complex.b == 0:
            return 'Real'
        elif complex.a == 0:
            return 'Imaginario puro'
        else:
            return 'Complejo'
    
    def pow(self, n):
        if(n < 1):
            return 'El exponente deber ser mayor que 0'
        if n == 1:
            return ComplexNumber(self.a , self.b)
        t_pow = self * self
        return t_pow.pow(n - 1)


complex0 = ComplexNumber()
complex1 = ComplexNumber(4, 5)
complex2 = ComplexNumber(-3, -2)
complex3 = ComplexNumber(-5, -3)
complex_eq = ComplexNumber(4, 5)
pure_complex = ComplexNumber(0, 1)

op1 = complex1 + complex2
op2 = complex1 - complex2
op3 = complex1 * complex2
op4 = complex1 / complex0
op5 = complex1 / complex2
op6 = complex1.pow(2)
op7 = complex1.pow(0)


print(f'Complejos:\n{complex0}\n{complex1}\n{complex2}\n')
print(f'Mod c1:\n{complex1.module}\n')
print(f'Suma:\n{op1}\n')
print(f'Resta:\n{op2}\n')
print(f'Mult:\n{op3}\n')
print(f'Div por 0:\n{op4}\n')
print(f'Div:\n{op5}\n')
print(f'Igualdad c1 y c2:\n{complex1 == complex2}\n')
print(f'Igualdad c1 y ceq:\n{complex1 == complex_eq}\n')
print(f'Tipo de c0:\n{ComplexNumber.is_pure(complex0)}\n')
print(f'Tipo de c1:\n{ComplexNumber.is_pure(complex1)}\n')
print(f'Tipo de pc:\n{ComplexNumber.is_pure(pure_complex)}\n')
print(f'Pot (2):\n{op6}')
print(f'Pot (0):\n{op7}')
