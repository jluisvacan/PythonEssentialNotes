"""
    Una funcion lambda es una funcion sin nombre, anonima.

    lambda parameters: expression

"""

#funcion que siempre devuelve 2
dos = lambda: 2

#funcion de un parametro que devuelve el valor de su argumento
sqr = lambda x: x * x

#funcion de dos parametros que devuelve el valor del primero elevado al segundo
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, dos()))

