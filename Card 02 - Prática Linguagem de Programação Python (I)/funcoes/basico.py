# Usamos def nome_função() para criar uma determinada função
# Podemos definir argumentos padrão, assim caso a pessoa não informe
# os parâmetros em especifico, os mesmos serão utilizados
def saudacao(nome = 'Pessoa', idade = 20):
    print(f'Bom dia {nome}!\nVocê nem parece ter {idade} anos!')
    
# def saudacao():
#     print('Boa tarde!')

# função com retorno, onde utilizamos return (var/operação)
def soma_e_multi(a, b, x):
    return a + b * x

# Verifica se esse foi o arquivo onde foi executado o programa
if __name__ == '__main__':
    saudacao('Ana', idade = 30)