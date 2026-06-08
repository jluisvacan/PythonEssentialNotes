"""
    La anulacion (overrading) anula la entidad definida despues [en el sentido de la herencia] de la misma entidad anterior.
    Las propiedades y metodos son priorizados el nivel superior de la herencia.

"""


class Level1:
    var = 100

    def fun(self):
        return 101


class Level2(Level1):
    var = 200

    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

#Dado que los nombres entre la subclase y superclase son iguales
#son priorizados el  nivel inmediato superior de la clase que esta invocando
#anulando las propiedades y metodos de la clase padre

print(obj.var, obj.fun())       # 200 201
