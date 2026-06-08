"""
    try-except permite intentar (try) ejecutar un bloque de codigo y si algo sale mal lanzar una excepcioin (except)

    try:
        :
        :
    except:
        :
        :
"""

number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo numero: "))

try:
    print(number1 / number2)
except:
    print("Esta operación no puede ser realizada.")

print("FIN.")
