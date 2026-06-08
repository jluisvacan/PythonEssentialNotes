"""
    La palabra reservada yield convierte la sentencia en un generador.
    A diferencia de return, que termina la ejecucion de la sentencia, yiled permite que la funcion devuelva un valor y pause su estado para reanidarlo mas tarde.
    Pausa y reanuda:
        Devuelve el valor
        Congela el estado actual
        Espera hasta que se solicite el siguiente valor

"""

#return termina la sentencia a penas iniciar, con valor 0
def fun(n):
    for i in range(n):
        return i

for i in range(5):
    print(fun(i))


#yield devuelve y mantiene el valor, yendo de 0 a 4
def func(n):
    for i in range(n):
        yield i

for v in func(5):
    print(v)

