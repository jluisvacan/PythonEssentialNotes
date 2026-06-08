"""
    Un constructor es una funcion dentro de la clase que:
        - tiene que ser nombrada de forma estricta
        - se invoca implicitamente cada que se crea un objeto

    class class_name:
        def _init_(self):
            ...

    el constructor siempre se llama _init_
    el constructor lleva al menos 1 parametro

    Para hacer un atributo privado de una clase, se agregan 2 guiones medios (__) antes del nombre de la propiedad
"""

# Se define la clase
class Constr:

    #Se define la función del constructor
    def __init__(self):
        print("¡Hola!")
        #Se agrega una propiedad al objeto
        self.constr_list = []
        #Se agrega una propiedad protegida al objeto
        self.__cons_list = []

# Se instancia el objeto
constr_object = Constr()

#Se valida longitud de propiedad constr_list
print(len(constr_object.constr_list))

#Se obtiene error al intentar acceder a la propiedad privada de constr_list
print(len(constr_object.__constr_list))