"""
    La funcion rmdir() permite eliminar el directorio especificado.
    La funcion listdir() lista los elementos del directorio relativo.

"""

import os

os.mkdir("my_first_directory")
print(os.listdir())
#os.rmdir("my_first_directory\\my_second_directory")
os.rmdir("my_first_directory")
print(os.listdir())