x = 10

# Enquanto x for diferente de 0
while x:
    print(x, end=' ')
    x -= 1

total = 0
qtde = 0
nota = 0.0

# Enquanto a nota for diferente de -1 (valor caso desejamos sair)
while nota != -1:
    # Pergunta a nota ou se queremos sair
    nota = float(input('\nInforme as notas ou -1 para sair: '))
    # Se a nota for diferente de -1 (não queremos sair)
    if nota != -1:
        qtde += 1
        total += nota
    
print(f'A média da turma é {total / qtde}!')