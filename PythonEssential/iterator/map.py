"""
    La funcion map() aplica la funcion pasada por su primer argumento a todos los elementos del segundo argumento
    Toma dos argumentos
        - una funcion
        - una lista
    Devuelve un iterador que entrega todos los resultados de funciones subsecuentes.

    map(function_name, sequence)
"""

#se crea lista de 0 a 4
list_1 = [x for x in range(5)]

#se aplica map para obtener el valor de operacion 2 ** x, para cada valor de list_1
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

#se aplica map para obtener el resultado de x * x , para cada valor de list_2
for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()