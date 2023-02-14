def square_of_n(n: int):
    '''Generator function for returning the square from 0 to n
    n: int | stop value
    '''
    for i in range(n+1):
        yield i ** 2

l = list(square_of_n(100))

print(l)

def factorial(n: int):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))