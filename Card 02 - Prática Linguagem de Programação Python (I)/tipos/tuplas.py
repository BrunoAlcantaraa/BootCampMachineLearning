nomes = ('Bruno', 'Igor', 'Jefferson', 'Bruno')

print(type(nomes))
print(nomes)

estaNaLista = 'Bruno' in nomes

print(f'Bruno está na tupla? {estaNaLista}')

print(nomes[0])
print(nomes[0:3]) # entre 0 e 3
print(nomes[2:]) # 2 em diante
print(nomes[:2]) # até 2

print('Tamanho da tupla: ' + str(len(nomes)))

x = ('Bruno')
print(type(x))