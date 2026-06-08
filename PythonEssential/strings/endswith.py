"""
    El metodo endswith() comprueba si la cadena termina con el agumento especificado.
    Devolvera una respuesta boolean.

    Ejemplo:
        "example".endswith("e")
"""

chain = 'Hello World!'

#el metodo es key sensitive
print(chain.endswith("world!"))

print(chain.endswith("World!"))
