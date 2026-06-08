"""
    El metodo strftime() permite devolver la fecha y la hora en el formato especificado.
    Toma como argumento un string que especifica un formato que puede constar de directivas (cadena que consta del caracter % porcentaje y una letra minuscula o mayuscula).

"""

from datetime import date
from datetime import time
from datetime import datetime

#Fecha
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

#Hora
t = time(14, 53)
print(t.strftime("%H:%M:%S"))

#Fecha y Hora
dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))