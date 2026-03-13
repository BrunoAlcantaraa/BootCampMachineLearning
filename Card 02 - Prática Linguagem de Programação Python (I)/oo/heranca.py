class Carro:
    def __init__(self):
        self.__velocidade = 0 
        
    @property
    def velocidade(self):
        return self.__velocidade
        
    def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
    
    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade
    
# Sub-classe, onde nesse caso Uno herda de Carro
class Uno(Carro):
    pass

# Sub-classe, onde nesse caso Ferrari herda de Carro
class Ferrari(Carro):
    # Aqui há sobreposição do método acelerar da classe pai
    # Nesse exemplo ele acelera duas vezes mais
    def acelerar(self):
        super().acelerar
        return super().acelerar()

c1 = Carro()
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())