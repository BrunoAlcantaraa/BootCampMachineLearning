from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

# Função que soma dois parâmetros
somar = lambda a, b: a + b

# Retorna para a lista todos os alunos em que a nota é maior ou igual a 7
alunos_aprovados = [aluno for aluno in alunos if aluno['nota' >= 7]]

# Retorna para a lista todos os alunos em que a nota é maior ou igual a 7
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]

# Passa a função soma por todo a lista nota_alunos_aprovados, assim
# as acumulando para retornar em apenas um resultado
total = reduce(somar, notas_alunos_aprovados)

media = total / len(alunos_aprovados)

print(media)