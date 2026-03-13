from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

# Função lambda onde recebe como parâmetro aluno
# e retorna o resultado da exmpressão lógica
# "aluno['nota'] >= 7"
aluno_aprovado = lambda aluno: aluno['nota'] >= 7

# Função lambda onde recebe um aluno e obtem sua nota
obter_nota = lambda aluno: aluno['nota']

# Recebe a e b, e retorna a soma dos mesmos
somar = lambda a, b: a + b

# Através do filter, ele passa a determinada função lambda
# filtrando como o nome ja diz, os dados das mesmas
# Nesse caso filtrando e deixando apenas os alunos com nota
# superior ou igual a 7
# obs: list transforma tudo isso numa lista
alunos_aprovados = list(filter(aluno_aprovado, alunos))

# junta da função map e da lambda ele retorna a nota de todos
# os alunos e as coloca em uma nova lista
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))

# Com reduce passa a função de soma, acumulando todos os resultados
# para mostrar o total
total = reduce(somar, notas_alunos_aprovados)

media = total / len(alunos_aprovados)

print(media)