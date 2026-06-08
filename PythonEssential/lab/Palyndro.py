"""
    Un palindromo es una palabra que se lee igual hacia adelante y hacia atras (ejemplo: kayak)
    El programa pide al usuario algún texto.
    Comprueba si el texto introducido es un palíndromo e imprime el resultado.

"""

text = input("Ingresa un texto: ")

#Remover los espacios en el texto ingresado
text = text.replace(' ','')

#Revisar si la palabra es igual en ambos sentidos
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("Es un palíndromo")
else:
	print("No es un palíndromo")