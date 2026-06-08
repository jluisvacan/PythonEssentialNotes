"""
    Un anagrama es una nueva palabra formada tras reorganizar las letras de una palabra, usando todas las letras orginales exactamente una vez.
    El programa pide al usuario dos textos por separado.
    Comprueba si los textos ingresados son anagramas.

"""


str_1 = input("Ingresa el primer texto: ")
str_2 = input("Ingresa el segundo texto: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
if len(strx_1) > 0 and strx_1 == strx_2:
	print("Anagramas")
else:
	print("No son anagramas")