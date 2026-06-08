"""
    El metodo weekday() devuelve el dia de la semana como un numero entero
    Donde:
        0 es lunes
        6 es domingo

"""

from datetime import date

d = date(2019, 11, 4)
print(d.weekday())


#Un metodo similar es isoweekday(), donde 1 es lunes y 7 es domingo
d = date(2019, 11, 4)
print(d.isoweekday())
