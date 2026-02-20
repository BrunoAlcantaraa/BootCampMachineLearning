x = 10

while x:
    print(x, end=' ')
    x -= 1

total = 0
qtde = 0
nota = 0.0

while nota != -1:
    nota = float(input('\nInforme as notas ou -1 para sair: '))
    if nota != -1:
        qtde += 1
        total += nota
    
print(f'A média da turma é {total / qtde}!')