"""
    El metodo replace() devuelve una copia de una cadena reemplazando las apariciones del primer argumento por el segundo argumento.
    Genera una cadena modificada.

    Ejemplo:
        "example".replace("example", "example2"))

"""

chain = " Hello World "

print(chain.replace("World", "City"))       # "Hello City"
print(chain.replace("World", ""))           # "Hello"


#La variante con tres parametros emplea el tercer parametro parea limitar el numero de reemplazos

print("Hello telephone!".replace("el", "a", 1))     # "Halo telephone!"
print("Hello telephone!".replace("el", "a", 2))     # "Halo taephone!"