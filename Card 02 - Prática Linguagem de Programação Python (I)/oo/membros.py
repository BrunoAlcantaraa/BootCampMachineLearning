class Contador:
    contador = 0 # atributo de classe
    
    def inst(self):
        return 'Estou bem!'
    
    # Método de classe, aonde não precisamos instanciar para uso, mas precisamos 
    # passar a classe (vamos se dizer assim)
    @classmethod 
    def inc(cls):
        cls.contador += 1
        return cls.contador
    
    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador
    
    # Método Estático, aonde não precisamos instanciar para uso também, mas diferente
    # do de classe, é livre de cls e self
    @staticmethod
    def mais_um(n):
        return n + 1
    

print(Contador.inc()) 
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
print(Contador.mais_um(99))