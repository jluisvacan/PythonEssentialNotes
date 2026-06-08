"""
    El metodo join() realiza una union de los elementos de una lista recibida como argumento [caso contrario provocara un TypeError].
    Genera una cadena con los elementos de la lista proporcionada.
    La cadena desde la que se invoca el motodo join sera usada como separador entre los elementos de la lista.

    Ejemplo:
        "example".join(array)

"""

array = ["blue", "red", "green"]

print(".".join(array))      # "blue.red.green"