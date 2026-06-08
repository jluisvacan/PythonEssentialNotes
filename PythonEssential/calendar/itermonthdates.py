"""
    El metodo itermonthdaters() devuelve un iterador.
    Devuelve todos los dias del mes y añó especificados, contemplando meses completos iniciando desde el primer dia de la semana.
    Requiere especificar el añó y el mes.

"""

import calendar

c = calendar.Calendar()

for date in c.itermonthdates(2025, 11):
    print(date, end=" ")


