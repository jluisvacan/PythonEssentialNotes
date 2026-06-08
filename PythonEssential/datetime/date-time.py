"""
    La clase datetime del modulo datetime permite representar como objetos la fecha y la hora.
    Admite los parametros:
        datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)

"""

from datetime import datetime, timezone

print("hoy:", datetime.today())
print("ahora:", datetime.now())
print("utc_ahora:", datetime.now(timezone.utc))