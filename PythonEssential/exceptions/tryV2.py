"""
    La variante de try-except permite intentar (try) ejecutar un bloque de codigo y dependiendo del tipo de Error obtenido lanzar una excepcioin (except) en especifico

    try:
        :
    except exc1:
        :
    except exc2:
        :
    except:
        :

    El orden de las excepciones (exc) importa, no colocar excepciones mas generales antes que otras concretas
"""

try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero..")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")