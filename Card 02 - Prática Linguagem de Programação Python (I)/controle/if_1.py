nota = float(input('Informe a nota do aluno: '))

# Passa "true" para comportado se o input for "s" e "false" se for outra coisa sem ser "s"
comportado = True if input('Comportado (s/n):') == 's' else False

# Se nota for maior ou igual que 9 e o aluno for comportado
if nota >= 9 and comportado:
    print('Duas palavras: para bens! :P')
    print('Quadro de Honra!')
# Se nota for maior ou igual a 7
elif nota >= 7:
    print('Aprovado!')
# Se a nota for maior ou igual a 5.5
elif nota >= 5.5:
    print('Recuperação!')
# Se a nota for maior ou igual a 3.5
elif nota >= 3.5:
    print('Recuperação + Trabalho!')
# Se não for nenhum do casos
else:
    print('Reprovado!')
    
print(nota)