"""
    El metodo find() busca una subcadena con el agumento especificado.
    Devuelve el indice donde se encontra la 1ra coincidencia.
    Solo aplica para cadenas, ninguna otra secuencia.

    Ejemplo:
        "example".find("e")

"""

chain = 'Hello World!'

#si no se encuentran coincidencias el metodo regresa -1
print(chain.find("z!"))

#el metodo es key sensitive
print(chain.find("world!"))

print(chain.find("World!"))


#La variante de dos parametros permite indicar el indice donde comenzar la busqueda
print(chain.find("World!", 4))


#La variante de tres parametros permite agregar un limite superior a la busqueda
print(chain.find("o", 6, 9))