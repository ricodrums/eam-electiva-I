class Fraction:
    def __init__(self, num, den) -> None:
        self.num = num // self.gcm(num, den)
        self.den = den // self.gcm(num, den)

    @staticmethod
    def gcm(a, b):
        if a < b:
            a, b = b, a
        if a == 0:
            return b
        if b == 0:
            return a
        return Fraction.gcm(b, a%b)

    def __add__(self, frac):
        num = self.num * frac.den + self.den * frac.num
        den = self.den * frac.den
        return Fraction(num, den)

    def __sub__(self, frac):
        num = self.num * frac.den - self.den * frac.num
        den = self.den * frac.den
        return Fraction(num, den)

    def __mult__(self, frac):
        num = self.num * frac.num
        den = self.den * frac.den
        return Fraction(num, den)

    def __truediv__(self, frac):
        num = self.num * self.den
        den = self.den * frac.num
        return Fraction(num, den)

    def __str__(self):
        return f'{self.num}\n---\n{self.den}'

f1 = Fraction(25, 30)
f2 = Fraction(40, 45)

print (f1 + f2)
print()

print (f1 - f2)
print()

print (f1 * f2)
print()

print (f1 / f2)
print()