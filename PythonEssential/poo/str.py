"""
    El metodo __str__() convierte elk contenido de un objeto en una cadena.

    class class_name:
        def __init__(self):
            ...

        def __str__(self):
            ...

"""


class Mouse:
    def __init__(self, name):
        self.my_name = name


    def __str__(self):
        return self.my_name


the_mouse = Mouse('mickey')
print(the_mouse)

