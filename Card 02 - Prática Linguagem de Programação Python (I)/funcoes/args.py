# Utilizamos *var para passar uma tupla, lista, conjunto etc
def soma(*nums): # tupla
    total = 0
    for n in nums:
        total += n
    return total

# Utilizamos **var para passar um dicionário
def resultado_final(**kwargs): 
    status = 'aprovado(a)' if kwargs['nota']  >= 7 else 'reprovado(a)'
    return f'{kwargs["nome"]} foi {status}'