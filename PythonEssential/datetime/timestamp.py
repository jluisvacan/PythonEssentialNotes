"""
    El metodo timestamp() proporciona una marca de tiempo en funcion de una fecha y hora determinadas.
    Devuelve un valor flotante.

"""

from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())
