"""
    raise es una palabra reservada que general exepcion especifica como si se hubiera generado de forma normal
    Permite simular la exepciones reales y parcialmente manejar la excepcion

    raise exc

"""

def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("¿Un error?")

print("FIN.")
