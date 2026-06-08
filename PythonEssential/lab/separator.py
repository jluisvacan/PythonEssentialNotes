"""
    Función que se comporta casi como el metodo split() :

        Acepta únicamente un argumento (una cadena).
        Devuelve una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
        Si la cadena ingresada está vacía, la función devuelve una lista vacía.
"""


def mysplit(chain):

    #Devuelve un array vacio [] si la cadena está vacía o solo contiene espacios en blanco
    if chain == '' or chain.isspace():
        return [ ]

    #Inicializa el array
    arry = []

    #Prepara una variable para construir las palabras subsecuentes
    word = ''

    #Verifica si la cadena ingresada comienza con una palabra
    inword = not chain[0].isspace()

    #Itera a través de todos los caracteres en cadena
    for x in chain:

        # si actualmente esta dentro de una cadena
        if inword:
            # y el caracter actual no es un
            if not x.isspace():
                # se actualiza la palabra actual
                word = word + x
            else:

                # De lo contrario, es el final de la palabra, y se agrega a la lista
                arry.append(word)

                # y señala que estamos ahora fuera de la palabra
                inword = False
        else:

            # si estamos fuera de la palabra y llegamos a un carácter no que no es un espacio en blanco
            if not x.isspace():
                # significa que ha comenzado una nueva palabra, por lo que debemos recordarla y...
                inword = True
                # ... almacenar la primera letra de la nueva palabra
                word = x
            else:
                pass
    # si hemos dejado la cadena y hay una cadena no vacía en la variable word, necesitamos actualizar la lista
    if inword:
        arry.append(word)
    # devolver la lista al invocador
    return arry


print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

