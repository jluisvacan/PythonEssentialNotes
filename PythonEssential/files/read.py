"""
    La funcion read() dekl objeto stream extrae datos del propio stream.
    Dependiendo de como se haya abierto el flujo puede devolver una cadena de texto o un objeto de bytes

    Lectura completa -> Se invoca sin argumentos, intenta leer y devolver el contenido
    Lectura pacial -> Recibe un argumento entero que especifica el numero maximo de bytes o caracteres qeu se deben leer

"""

from os import strerror

try:
    counter = 0
    stream = open('text.txt', "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))
