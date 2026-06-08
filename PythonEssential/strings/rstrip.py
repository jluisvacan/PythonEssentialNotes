"""
    El metodo rstrip(), similar a lstrip(), devuelve una copia de una cadena eliminando todos los espacios en blanco al final de la cadena.
    Devuelve una cadena.

    Ejemplo:
        "example".rstrip()

"""

chain = " Hello World, Goodbye "

print("[" + chain.rstrip() + "]")       # " Hello World, Goodbye"

#Al agregar un argumento, se elimina todos los caracteres que coincidan con el argumento, eliminando caracteres no subcadenas
chain2 = "Hello World"
print("[" + chain2.rstrip(" World") + "]")       # "He"
