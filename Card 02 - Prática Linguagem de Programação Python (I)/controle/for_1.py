# For com um único parâmetro, onde informa quantas vezes irá incrementar a variavel
# Nesse caso, i vai de 0 a 9
for i in range(10):
    print(i, end=' ')
    
print('')
    
# For com 2 parâmetros, onde no primeiro se passa o valor inicial a variavel
# e no segundo, até onde o valor da variavel deve ir
# Nesse caso, i vai de 1 a 10
for i in range(1, 11):
    print(i, end=' ')

print('')
    
# For com 3 parâmetros, onde os dois primeiros funcionam como no exemplo anterior, e o
# terceiro especificamos o quanto queremos incrementar por ciclo na variavel
# Nesse caso, i vai do 1 até 99 incrementando de 7 em 7
for i in range(1, 100, 7):
    print(i, end=' ')
    
print('')
    
# Mesmo que exemplo anterior, só que com o primeiro e segundo parâmetro invertidos, assim
# fazendo ele contar regressivamente
# Nesse caso, i vai do 20 ao 0 decrementando 3 por ciclo
for i in range(20, 0, -3):
    print(i, end=' ')
    
print('')
    
nums = [2, 4, 6, 8]

# Exemplo de foreach, onde criamos uma variavel e especificamos a lista
# que desejamos percorrer
for n in nums:
    print(n, end=' ')
    
print('')
    
texto = 'Python é muito massa!'

# Outro foreach, onde ele passa por toda uma String informando seus caracteres
# no caso, a String funciona como uma lista
for letra in texto:
    print(letra, end=' ')

print('')
    
# Foreach em que o conjunto é especificado dentro do for
for n in {1, 2, 3, 4, 4, 4}:
    print(n, end=' ')
    
print('')    

produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

# Foreach em que podemos passar um dicionário e passar por seus atributos
for atrib in produto:
    print(atrib, '==>', produto[atrib], end=' ')

print('')    
    
# Foreach com dicionario.items() onde ele passa os atributos e seus valores
# para as variaveis especificadas
for atrib, valor in produto.items():
    print(atrib, '==>', valor, end=' ')

print('')    
    
# Foreach que passa pelos valores dos atributos de um dicionário
for valor in produto.values():
    print(valor, end=' ')
    
print('')    
    
# Foreach que passa pelos atributos de um dicionário, parecido com o exemplo do "for atrib in produto:"
for atrib in produto.keys():
    print(atrib, end=' ')    