"""
    La funcion makedirs() permite crear otro directorio dentro del que se acaba de crear, de manera recursica crea directorios

    os.makedirs("dir1/dir2")

"""

import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())
