"""
    El metodo replace() permite modificar un objeto de tipo date

"""

from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)
