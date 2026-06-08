"""
    La funcion removedir() permite eliminar todos los directorios de una ruta especificada.

"""

import os

os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())

