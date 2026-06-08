"""
    La clase fromtimestamp del modulo datetime proporciona una fecha a partir de una marca de tiempo (1 de Enero de 1970 a las 00:00:00 UTC)
    La funcion time del modulo time devuelve un numero de segundos desde 1 de enero de 1970 hasta el momento actual en formato flotante
"""

from datetime import date
import time

timestamp = time.time()
print("Marca de tiempo:", timestamp)

d = date.fromtimestamp(timestamp)
print("Fecha:", d)
