"""
    El metodo readinto() lee bytes desde un stream directamente, no crera un nuevo objeto sino que llena un espacio creado previamente con los valores tomados del archivo binario.
    Devuelve el numero de bytes leidos con exito.



"""

from os import strerror

data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
