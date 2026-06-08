"""
    La clase date del modulo datetime representa una fecha que cosnta de un año, mes y dia.
    La funcion today() permite obtgener la fecha local actual

    date.today()
"""

from datetime import date

today = date.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)


#Para crear un objeto del tipo date es necesario pasar los parametreos año, mes y dia
my_date = date(2019, 11, 4)
print(my_date)
