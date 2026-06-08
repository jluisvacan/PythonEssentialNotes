"""
    El metodo isalnum() valida que la cadena contine digitos alfanumericos.
    Devuelve un valor booleano.

    Ejemplo:
        "example".isalnum()

"""


chain = 'HelloWorld'
chain2 = 'Hello World'
number = '123'

print(chain.isalnum())      #True
print(chain2.isalnum())      #False
print(number.isalnum())     #True
