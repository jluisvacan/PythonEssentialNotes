"""
    La variable __name__ contiene el nombre del archivo excluyendo .py
    Util para identificar el contexto donde se activo
"""

counter = 0

if __name__ == "__main__":
    print("Prefiero ser un módulo.")
else:
    print("Me gusta ser un módulo.")

