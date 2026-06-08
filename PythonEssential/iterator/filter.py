"""
    La funcion filter() filtra los elementos de una secuencia basandose en una condicion.
    Devuelve una coleccion que contenga unicamente los elementos que cumplan el criterio


    filter(function, sequence)
"""


from random import seed, randint

seed()
#se obtienen arrat de datos aleatorios
data = [randint(-10,10) for x in range(5)]

#se filtran los datos que cunplan las condiciones x > 0 and x % 2 == 0
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)