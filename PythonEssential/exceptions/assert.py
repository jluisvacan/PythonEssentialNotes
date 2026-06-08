"""
    la palabnra reservada assert evalua la expresion:
        si la expresion se evalua como True no hara nada mas
        si la expresion se evalua como False se genera una exception llamada AssertionError

    assert expression

"""

import math

x = float(input("Ingresa un número: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)