"""
    Sudoku es un ronmpecabezas de colocacion de numeros jugado en un tablero de 9x9. El jugador tiene que llenar el tablero de manera especifica:
        - Cada fila del tablero deber contenero todos los digitos del 0 al 9
        - Cada columna del tablero debe de contener todos los digitos del 0 al 9
        - Cada uno de los 9 subcuadros de 3x3 de la tabla debe contener todos los digitos del 0 al 9.

    El programa lee las 9 filaas del Sudoku, cada una con 9 digitos.
    Da como salida SI si el Sudoku es valido y NO de lo contrario.

"""


# Una función que verifica si una lista pasada como argumento contiene nueve dígitos del '1' al '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# Una lista de filas que representan el Sudoku.
rows = []
for r in range(9):
    ok = False
    while not ok:
        row = input("Ingresa fila #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Datos de fila incorrectos: se requieren 9 dígitos")
    rows.append(row)

ok = True

# Comprobar si todas las filas son correctas.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Comprobar si todas las columnas son correctas.
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Comprobar si todos los subcuadrados (3x3) son correctos.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Hacer una cadena que contenga todos los dígitos de un subcuadrado.
            for i in range(3):
                sqr += rows[r + i][c:c + 3]
            if not checkset(list(sqr)):
                ok = False
                break

# Imprimir el veredicto final.
if ok:
    print("Si")
else:
    print("No")
