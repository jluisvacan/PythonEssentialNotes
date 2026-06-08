"""
    Un stream es una secuencia de elementos de datos que se ponene a disposicion de forma progresiva a lo largo del tiempo.
    Modos de abrir un stream
        r -> modo de apertura: lectura
        w -> modo de apertura: escritura
        a -> modo de apertura: adjuntar
        r+ -> modo de apertura: lectura y actualizacion
        w+ -> modo de apertura: escritura y actualizacion

    los nombres de los streams son:
        - stdin
            Entrada estandar
        - stdout
            salida estandar
        - stderr
            error estandar
"""

import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Procesamiento.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:
        print("Demasiados archivos abiertos.")
    else:
        print("El numero del error es:", exc.errno)
