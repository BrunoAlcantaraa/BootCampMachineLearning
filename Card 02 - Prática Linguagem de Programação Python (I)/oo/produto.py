
class Produto:
    # Como se fosse o construtor em java
    def __init__(self, nome, preco = 1.99, desc = 0):
        # Como se fosse o this do java (self)
        self.nome = nome 
        self.__preco = preco # deixa privado, porem ainda dá para acessar com _Produto__preco
        self.desc = desc
        
    @property # pois é como se fosse um atributo
    def preco(self):
        return f'R$ {self.__preco}'
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0.0:
            self.__preco = novo_preco
        
    def preco_final(self): # deixado sem property pra mostrar
        return self.__preco * (1 - self.desc)

p1 = Produto('Caneta', 10, 0.1)
p2 = Produto('Caderno', 14, 0.5)

p1.preco = -70
p2.preco = 1.99

print(p1.nome, p1.preco, p1.desc, p1.preco_final())
print(p2.nome, p2.preco, p2.desc, p2.preco_final())