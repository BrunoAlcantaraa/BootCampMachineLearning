
pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']

# Passa por todas as pessoas
for p in pessoas:
    # Passa pelos adjetivos
    for a in adjs:
        print(f'{p} é {a}!')
# No caso ele vai passar por todas as pessoas e falar todos os adjetivos para cada um


# Adicionamos pass no for caso queiramos deixar vazio        
for i in [1, 2, 3]:
    pass # Caso seja um for vazio

# Usamos continue para passar para o proximo ciclo do for
for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)
    
# utilizamos break para sair do loop total quando queiramos
for i in range(1, 11):
    if i == 5:
        break
    print(i)
    
print('Fim!')