"""
   La funcion setfirstweek permite modificar el primer dia de la semana, por defecto el primer dia es el lunes.

"""

import calendar

#Se define SUNDAY como primer dia de la semana
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)