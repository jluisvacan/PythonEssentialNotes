"""
    El metodo lstrip() devuelve una copia de una cadena eliminando todos los espacios en blanco iniciales.
    Genera una cadena sin espacios iniciales.

    Ejemplo:
        "example".lstrip()

"""

chain = " Hello World "
chain2 = "Hello World!"

print(chain)                # " Hello World "
print(chain.lstrip())       # "Hello World "


#El metodo con 1 parametro elimina todos los caracteres incluidos en el argumento, no solo espacios en blanco
#Al agregar un argumento, se elimina todos los caracteres que coincidan con el argumento, eliminando caracteres no subcadenas

print(chain2.lstrip("Hello"))   # "World!"

#El metodo elimina del extremo izquierdo (inicio) del argumento
print(chain2.lstrip("World!"))   # "Hello World!"