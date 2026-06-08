"""
    La funcion getcwd() brinda la ruta absoluta del directorio de trabajo actual.
    La funcion mkdir() permite cambiar el directorio de trabajo actual.
"""

import os

#os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())
