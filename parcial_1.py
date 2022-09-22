from typing import List
from math import sqrt

'''
Parcial 1
Presentado por Jhonatan David Rico Echeverri - 240220222007
'''
print(
'''
(1.5 puntos) Desarrolle un algoritmo que almacene en una lista las siguientes asignaturas: Inglés, Matemáticas,
Geografía, Filosofía, Lenguaje y Estádistica. Se debe preguntar al usuario cuál es la nota obtenida en cada
materia (float) y eliminar de la lista de materias aquellas ganadas (nota>= 6). Finalmente mostrar cuáles
asignaturas se deben repetir.

''')
asignaturas: List[str] = ['Inglés', 'Matemáticas', 'Geografía', 'Filosofía', 'Lenguaje', 'Estádistica']
reprobadas: List[str] = []
print(f'Asignaturas: {asignaturas}')
for index, asignatura in enumerate(asignaturas):
    nota: float = -1
    while nota > 10 or nota < 0:
        nota = input(f'Ingrese la nota de {asignatura}: ')
        try:
            float(nota)
        except ValueError:
            print("No puede ingresar valores que no sean numericos")
            nota = -1
        else:
            nota = float(nota)
        if nota < 6 and nota > -1:
            reprobadas.append(asignatura)
            index -= 1
            
print(f'Debe re cursar: {reprobadas}')
print()
print(
'''
(1.5 puntos) Escriba un programa que guarde en una lista el abecedario, luego elimine de esa lista las letras
que ocupen posiciones que sean múultiplos de 3.
EJEMPLO
Entrada: abcdefghijk
Salida: abdeghj...
''')

abc: List[str] = list('abcdefghijklmnopqrstuvwxyz')
ab: List[str] = []
print(f'Abecedario {abc}')
for i, l in enumerate(abc):
    i += 1
    if not i%3 == 0:
        ab.append(l)
print(f'Abecedario\' {ab}')
print()
print(
'''
(2.0 puntos) Escriba una rutina que reciba una lista de números separados por comas; luego calcule la
media y la desviación estándar de esos números.
EJEMPLO
Entrada: 1, 2, 3, 4, 5
Salida: media=3.0; desviación: 1.4142
''')
numeros: List[str]
lista: str = input('Ingrese una lista de numeros separados por comas (,). Nota, tenga cuidado al ingresar los datos, no se hace ningun tipo de validacion:\n')
numeros = lista.split(',')
suma: int = 0
suma2: int = 0
total_nums = len(numeros)
for n in numeros:
    n = float(n)
    suma += n
    suma2 += n*n

media: float = suma/total_nums
desviacion: float = sqrt((suma2/total_nums) - (media*media))
desviacion = round(desviacion, 4)

print(f'La media es {media}')
print(f'La desviacion estandar es {desviacion}')
