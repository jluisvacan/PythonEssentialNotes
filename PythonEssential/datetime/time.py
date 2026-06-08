"""
    La clase time del modulo datetime permite presentar la hora.
    Puede recibir los siguientes argumentos:
        time(hour, minute, second, microsecond, tzinfo, fold)

"""

from datetime import time

t = time(14, 53, 20, 1)

print("Tiempo:", t)
print("Hora:", t.hour)
print("Minutos:", t.minute)
print("Segundos:", t.second)
print("Microsegundo:", t.microsecond)