"""
    La funcion write() escribe en un archivo abierto, recibe un argumento un string que se transfiere a un archivo abierto.
    No añade un salto de linea automaticamente.


"""

from os import strerror

try:
    # Se crea un nuevo archivo (newtext.txt)
    file = open('newtext.txt', 'wt')
    for i in range(10):
        # Se escribe en el nuevo archivo
        file.write("línea #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))