"""
    La funcion readlines() de los objetos strem se invoca sin argumentos lee el contenido copleto del stream y lo divide automaticamente en una lista de cadenas de texto
    Devuelve un array de cadenas, un elemento por linea del archivo

"""

file = open("text.txt", "r")
# Lee todo y crea un array
lines = file.readlines()

# Muestra cuántas líneas tiene el archivo
print(len(lines))

# Imprime la primera línea con su salto de línea
print(lines)
file.close()