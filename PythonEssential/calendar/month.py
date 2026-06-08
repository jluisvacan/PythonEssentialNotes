"""
    La funcion month() del modulo calendar muestra el calendario para un mes especificado.


"""

import calendar

print(calendar.month(2026, 11))


#Alternativamente, la funcion prmonth() muestra el mes indicado sin la necesidad de la funcion print()
calendar.prmonth(theyear=2026, themonth=11)