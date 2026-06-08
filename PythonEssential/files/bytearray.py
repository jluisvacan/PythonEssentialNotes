"""
    Un bytearray es un array que contiene bytes. Recibe como parametro un numero entero

    Un dato amorfo son datos que no tienen forma especifica, solo una seria de bytes

    data = bytearray(n)


"""

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))
