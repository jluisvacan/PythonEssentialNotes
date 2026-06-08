"""
    El metodo rfind(), al igual que find(), busca una subcadena con el agumento especificado comenzando sus busquedas desde el final de la cadena.
    Devuelve el numero de indice donde encuentra el argumento proprocionado.

    Ejemplo:
        "example".rfind("ple"))

"""

chain = "Hello Hello Hello"

#Se indica el argumento de la busqueda
print(chain.rfind("Hello"))                                         # 12
#Se indica el argumento y el indice del inicio de la busqueda
print(chain.rfind("Hello", 5))                          # 6
#Se indica el argumento, el indice del inicio y fin de la busqueda
#El valor -1 indicas que el argumento no se encontro en la cadena
print(chain.rfind("Hello", 5, 10))                # -1