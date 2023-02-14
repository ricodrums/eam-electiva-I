from typing import List

print('''
1. Escriba una función en Python que indique si un número está en un determinado intervalo (solución).
Entrada: valor=3; lim_inferior=2; lim_superior=5
Salida: True
''')
a = b = c = ''
print(a, b, c)
while (not a.isnumeric()):
    a = input('Ingrese un numero:\n')
while (not b.isnumeric()):
    b = input('Ingrese el numero maximo:\n')
while (not c.isnumeric()):
    c = input('Ingrese el numero minimo:\n')
a = int(a)
b = int(b)
c = int(c)

def is_between(n: int, top: int, bottom: int):
    return bottom <= n and top >= n

print(is_between(a, b, c))


print('''
2. Escriba una función en Python que reciba una lista de valores enteros y devuelva otra lista sólo con aquellos valores pares (solución).
Entrada: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Salida: [2, 4, 6, 8]
''')
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def only_pairs(n_list: List[int]):
    return [n for n in n_list if n %2 == 0]

print(only_pairs(numbers))

print('''
3. Escriba una función en Python que indique si un número es perfecto. Utilice una función auxiliar que calcule los divisores propios (solución).
Entrada: 8128
Salida: True
''')
n = ''

while(not n.isnumeric()):
    n = input('Ingrese un numero positivo:\n')

n = int(n)

def is_perfect(num: int):
    return sum(get_divisors(num)) == num

def get_divisors(num: int):
    return [(x + 1) for x in range(int(num/2)) if num%(x+1) == 0]

if n == 0:
    print(False)
else:
    print(is_perfect(n))

print('''
4. Escriba una función en Python que determine si una cadena de texto es un palíndromo (solución).
Entrada: ana lava lana
Salida: True
''')
word = input('Ingrese una palabra:\n')

def es_palindromo(w: str):
    return w == w[::-1]

print(es_palindromo(word))

print('''
5. Escriba una función en Python que determine si una cadena de texto es un pangrama (solución)
Entrada: The quick brown fox jumps over the lazy dog
Salida: True
''')
word = input('Ingrese una oracion:\n')
abc = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')

def es_pangrama(w: str):
    for l in w:
        print(abc)
        if l in abc:
            abc.remove(l)
    return len(abc) == 0

print(es_pangrama(word))
