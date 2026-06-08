"""
    El digito de la Vida es un digito calculado usando el cumpleanos de alguien, solo se neceita sujmar los digitos de la fecha.
    Si el resultado contiene mas de un digito se debe de repetir la suma hastga obtener un exactamente un digito.

    El programa pide al usuario ingresar su fecha de cumplenos.
    Devuelve el digito de la vida de la fecha ingresada.

"""

date = input("Ingresa la fecha de nacimiento [en formato AAAAMMDD]: ")
if len(date) != 8 or not date.isdigit():
    print("Formato de fecha incorrecto")
else:
    while len(date) > 1:
        date_sum = 0
        for i in date:
            date_sum = date_sum + int(i)
        print("Fecha ingresada: ", date)
        date = str(date_sum)

    print("El numero de la vida es: " + date)