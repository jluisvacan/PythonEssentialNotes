"""
    El digito de la Vida es un digito calculado usando el cumpleanos de alguien, solo se neceita sujmar los digitos de la fecha.
    Si el resultado contiene mas de un digito se debe de repetir la suma hastga obtener un exactamente un digito.

    El programa pide al usuario ingresar su fecha de cumplenos.
    Devuelve el digito de la vida de la fecha ingresada.

"""

word = input("Ingresa la palabra que deseas encontrar: ").upper()
strn = input("Ingresa la cadena en donde deseas buscar: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start)
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Si")
else:
	print("No")