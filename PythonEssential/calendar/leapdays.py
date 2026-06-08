"""
    El metodo leapdays() permite identificar si uin año es bisiesto.
    Devuelve el numero de años bisiestos en el rango de añós especificado

"""

import calendar

print(calendar.leapdays(2010, 2026))  # Hasta 2021, pero sin incluirlo.
