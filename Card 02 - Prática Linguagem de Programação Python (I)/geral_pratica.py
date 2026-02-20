
#################
## COMENTÁRIOS ##
#################
# Para criar podemos utilizar tanto # quanto """

# Exemplo

"""
Exemplo
"""


##########################
## IMPORTAR BIBLIOTECAS ##
##########################
# Para importar bibliotecas podemos utilizar dois formatos:

import tipos.variaveis
from tipos import variaveis


###############
## VARIAVEIS ##
###############
# O Python é uma linguagem não tipada, portanto podemos declarar
# varias variaveis apenas mudando o que atribuimos a elas:

num = 1
nome = 'Josimar'
nota = 9.9


###############
## IMPRESSÃO ##
###############
# Para se imprimir algo na tela usamos o comando "print"

# Podemos ver os tipos de diferentes variaveis dessa forma:
print(type(nome)) # No caso, String

# Para printar uma variavel que não seja String podemos fazer:
print('Nota: ' + str(nota))

# Outra forma de print:
print(f'num: {num}')


############
## LISTAS ##
############
# Para criar:
lista = [1, 2, 3] 

# Para adicionar:
lista.append(5)

# Para trocar um determinado valor
lista[3] = 4

# Para inserir um determinado valor depois de um index
lista.insert(0, 0)


############
## TUPLAS ##
############
# Após a criação não é possivel adicionar
# outros valores.

# Para criar:
tupla = (1, 2, 3) 

# Para verificar se um determinado valor esta presente podemos:
estaNaTupla = 1 in tupla


###############
## CONJUNTOS ##
###############
# Não aceita repetições.

# Para criar:
conjunto = {1, 2, 3} 

# Para adicionar:
conjunto.add(4)


#################
## DICIONÁRIOS ##
#################
# Para criar:
dicionario = {
    'lingua': 'Português',
    'autor': 'Bruno Alcantara',
    'Ano': 2026
}

# Para acessar um atributo:
print('Linguagem do dicionário: ' + dicionario['lingua'])


################
## OPERADORES ##
################

# * UNARIOS *
# Envolvem uma unica "condição"
var = not False
print(f'Meu nome é Bruno? {var}')

num = 3
num = -num
print(f'Negativo de 3 é {num}')


# * ARITMÉTICOS *
# Para cálculos
soma = 1 + 1
print(f'Soma de 1 + 1: {soma}')
sub = 1 - 1
print(f'Subtração de 1 - 1: {sub}')
mult = 1 * 1
print(f'Multiplicação de 1 * 1: {mult}')
div = 1 / 1
print(f'Divisão de 1 / 1: {div}')
resto = 1 % 1
print(f'Resto de 1 / 1 (1 % 1): {resto}')


# * RELACIONAIS *
# Para comparações
x = 10
y = 20

igual = x == y
print(f'X({x}) == Y({y}): {igual}')
dif = x != y
print(f'X({x}) != Y({y}): {dif}')
maior = x > y
print(f'X({x}) > Y({y}): {maior}')
menor = x < y
print(f'X({x}) < Y({y}): {menor}')

# * ATRIBUIÇÃO * 
# Formas de "manipular" as variaveis
x = 0

# ADD
x += 1
print(f'Incremento em x: {x}')

# SUB
x -= 2
print(f'Decremento em x: {x}')

# MULT
x *= 5
print(f'Multiplicação em x: {x}')

# DIV
x /= 2
print(f'Divisão em x: {x}')

# RESTO
x %= 2
print(f'Módulo em x: {x}')


# * LÓGICOS *
# Definem "True" ou "False"
verdade = True
mentira = False

print(f'Verdade & verdade: {verdade and verdade}')
print(f'Mentira & mentira: {mentira and mentira}')
print(f'Verdade & mentira: {verdade and mentira}')

print(f'Verdade | verdade: {verdade or verdade}')
print(f'Mentira | mentira: {mentira or mentira}')
print(f'Verdade | mentira: {verdade or mentira}')

print(f'Verdade & NÃO verdade: {verdade and not verdade}')
print(f'NÃO Mentira | mentira: {not mentira or mentira}')


# * TERNARIO *:
# "Três partes"
temBrilho = True

        # "1 parte"    # "2 parte"         # "3 parte"
fala = 'É uma jóia!' if temBrilho else 'Vix, é só uma pedra!'
print(fala)

idade = 19
maiorIdade = True if idade >= 18 else False
print(f'É maior de idade? {maiorIdade}')


# * CONDIÇÃO *
# "IF"
alunoComportado = True

if alunoComportado:
    print('Muito bem, continue assim!')
else:
    print('Aí não dá né meu caro, melhora ai...')
    
idade = int(input('Digite sua idade: '))

if idade <= 8:
    print('Criança!')
elif idade <= 12:
    print('Pré-adolescente!')
elif idade <= 18:
    print('Adolescente!')
elif idade <= 50:
    print('Adulto!')
else:
    print('Idoso!')
  
    
###########   
## LOOPS ##
###########

### FOR ###
print('Contando até 10:')
for i in range(10):
    print(i, end=' ')
    
print('')
    
print('Contando de 1 até 10:')
for i in range(1, 11):
    print(i, end=' ')

print('')
    
print('Contando de 1 até 10 em 2 em 2:')
for i in range(1, 11, 2):
    print(i, end=' ')

print('')

alunos = ['Bruno', 'Igor', 'Jefferson', 'Marciano']
print('Lista de Alunos:')
for aluno in alunos:
    print(aluno)
    
nums = {1, 1, 2, 2, 3, 3}
print('Números de um conjunto:')
for num in nums:
    print(num)
    
moto = {
    'modelo': 'CG TITAN',
    'cilindrada': '160',
    'ano': '2019'
}

print('Características da Moto:')
for atrib in moto:
    print(atrib, ': ', moto[atrib])
    
print('\nCaracterísticas da Moto: [2]')
for atrib, valor in moto.items():
    print(atrib, ': ', valor)
    
print('\nAtributos da Moto:')
for atrib in moto.keys():
    print(atrib)
    
print('\nValores da Moto:')
for valor in moto.values():
    print(valor)
    
    
### WHILE ###
print('A bomba vai explodir em...')
tempo = 10

while tempo > 0:
    print(f'Explodindo em {tempo}...')
    tempo -= 1

print('BOOOOOOMMMM')

print('\nAté você não digitar \"sair\" você não sai daqui!')

texto = ""

while(texto != 'sair'):
    texto = input('Digite:')

print('Você saiu!')


#############
## Funções ##
#############
from funcoes import basico

# Quando importo a determinada classe, para utilizar alguma função dela uso:
basico.saudacao()

def acelerar(velocidade = 10): # quando coloco dessa forma, ajusto um valor padrão para a função caso não seja especificado o parâmetro
    print(f'Acelerando a {velocidade} KM/H...')
    
### Args ###
    
def calcularMediaNota(*notas): # Quando quero receber uma tupla uso o "*":
    totalNota = 0
    for nota in notas:
        totalNota += nota
    totalNota /= len(notas)
    return totalNota

def mostrarInfoPessoa(**pessoa): # Quando quero receber um "dicionário" uso "**"
    print(pessoa['nome'])
    print(pessoa['idade'])
    
mostrarInfoPessoa(nome = 'Bruno', idade = 19)

pessoa = {
    'nome': 'Katia',
    'idade': 38
}
mostrarInfoPessoa(**pessoa)

### Funcionais ###
def cumprimento(texto = 'Olá'):
    print(texto)
    def pedirAlgo(texto2 = 'Como está?'):
        print(texto2)
    return pedirAlgo
        
# Passo a função para uma var
cump = cumprimento()

# Chamando assim ela vai executar coms os valores pre-definidos
cump()

# Assim altero a função pedirAlgo dentro da cumprimento
cump('Como vai?')

# Outro ex:
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def calcular(calculo, a, b):
    if calculo == 'mais':
        fn = somar
    elif calculo == 'menos':
        fn = subtrair   
    print(fn(a, b))
    
calcular('mais', 1, 1)
calcular('menos', 1, 1)
        
#########
## Map ##
#########
def colocar_sobrenome(sobrenome):
    def colocar_nome(nome):
        return f'{nome} {sobrenome}'
    return colocar_nome

pessoas = ['Bruno', 'Katia', 'Josimar']

familia = list(map(colocar_sobrenome('Alcantara'), pessoas))

print(familia)

############
## Reduce ##
############
from functools import reduce

def juntar_nomes(nome_1, nome_2):
    return f'{nome_1}:{nome_2}'

nomes = ['Roberto', 'Maria', 'João']

nomes_juntos = reduce(juntar_nomes, nomes)

print(nomes_juntos)

############
## Lambda ##
############
pessoas = [
    {
        'nome': 'Bruno',
        'idade': 19
    },
    {
        'nome': 'José',
        'idade': 17
    }
]

de_maior_idade = lambda pessoa: pessoa['idade'] >= 18

pessoas_de_maior = list(filter(de_maior_idade, pessoas))

print(pessoas_de_maior)

###################
## Comprehension ##
###################
nums_ate_100 = [num for num in range(0, 101)]
print(nums_ate_100)

pessoas_de_maior2 = [pessoa for pessoa in pessoas if pessoa['idade'] >= 18]
print(pessoas_de_maior2)

########
## OO ##
########
class Pessoa():
    pessoas_no_mundo = 7000000000000 # atributo de classe
    
    # Como se fosse o construtor em java
    def __init__(self, nome, ano_nasc):
        self.__nome = nome # self como se fosse o this
        self.ano_nasc = ano_nasc
       
    @nome.setter # setter
    def nome(self, nome):
        if nome != '':
            self.__nome = nome
    
    @property # getter
    def nome(self):
        return self.__nome
       
    @property # define a função como se fosse um atributo, não precisando usar "()" no final
    def idade(self):
        return 2026 - self.ano_nasc
       
    @staticmethod # método estático, a qual pode ser acessado sem instância
    def cumprimentar():
        print('Olá!')
        
    @classmethod # método de classe, onde não depende da instância também
    def nasceu(cls):
        pessoas_no_mundo += 1
    
bruno = Pessoa('Bruno', 18)
Pessoa.cumprimentar()
Pessoa.nasceu()

class Bruno(Pessoa): # Sub-Classe, onde Bruno herda de Pessoa
    def __init__(self, nome, ano_nasc):
        super().__init__(nome, ano_nasc)
        
    def fazer_coisas_de_bruno():
        print('Oi, eu sou o Bruno!')