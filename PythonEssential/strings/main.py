"""
    Una cadena, al igual que una tupla, no puede ser modificada por medio de la subfuncion .append o .insert
    Pero las cadenas se pueden modificar mediante los operadores * y +
"""

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"
alphabet_2 = alphabet * 2

print(alphabet)
print(alphabet_2)