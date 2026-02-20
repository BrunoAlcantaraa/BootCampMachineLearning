#!python3

print('Bem vindo Bruno!')

print('-> main.py: (esse)')
print(__name__)
print(__package__)

print('-> arquivo.py:')
import pacote.sub.arquivo

print('-> comentarios.py:')
from tipos import comentarios # Outro jeito para importar classes/arquivos