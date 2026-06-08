"""
    La funcion hasattr permite verificar con seguriudad si algun objeto / clase contiene una propiedad especifica.
    Necesita de dos argumentos:
        - La clase o el nombre del objeto que se verifica
        - El nombre de la propiedad cuya existencia se desea validar
    Devuelve una respuesta boolean

    hasattr(example_object, 'attr')

"""


class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))        # True
print(hasattr(ExampleClass, 'prop'))        # False
