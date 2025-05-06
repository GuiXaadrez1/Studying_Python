'''

    Crie uma função que contabilizer os elementos replicados em uma lista
    E retorne a o elemetento e a quantidade de vezes que ele existe na lista
    Exemplo:
    
    abacaxi 2
    arroz 2
    feijão 3
    farofa 4

'''

# para resolver essa questão irei usar duas alternativas, uma com a lib collection
# outra sem essa lib

# usando a lib collection
from collections import Counter

def contar_repetidos_collection(lista):
    contagem = Counter(lista)
    for item, qtd in contagem.items():
        if qtd > 1:
            print(f"{item}: {qtd}")

# sem usar a lib collection

def contar_repetidos(lista):
    contagem = {}  # Inicializa um dicionário vazio para armazenar as contagens

    for item in lista:
        # Verifica se o item já existe como chave no dicionário
        if item in contagem:
            # Se sim, incrementa o valor (ocorrência) da chave em 1
            contagem[item] += 1
        else:
            # Se não, adiciona o item ao dicionário com valor inicial 1
            contagem[item] = 1

    # Percorre os pares chave-valor no dicionário
    for item, qtd in contagem.items():
        # Exibe apenas os itens que aparecem mais de uma vez
        if qtd > 1:
            print(f"{item}: {qtd}")

if __name__ == '__main__':

    # Exemplo de uso usando a lib collectio
    lista_string = ['Abacaxi','Arroz','Feijão','Pão','Abacaxi','Abacaxi',
                    'Pepino','Pepino','Pepino','Suco','Maçã','Uva']
    contar_repetidos_collection(lista_string)


    # Exemplo de uso sem a lib colection
    lista_string = ['Abacaxi','Arroz','Feijão','Pão','Abacaxi','Abacaxi',
                    'Pepino','Pepino','Pepino','Suco','Maçã','Uva']
    contar_repetidos(lista_string)
            
        