"""
    El polimorfismo es la capacidad en la que una misma clase puede tomar varias formas, dependiendo de las redefiniciones realizadas por cualquiera de sus subclases.
    El comportamiento de cualuier clase puede modificarse en cualquier momento.

"""

import time

class Tracks:
    def change_direction(self, left, on):
        print("pistas: ", left, on)

class Wheels:
    def change_direction(self, left, on):
        print("ruedas: ", left, on)

#La propiedad controller se pasa a la clase Tracks y Wheels durante la inicializacion mediante el constructor
class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)
