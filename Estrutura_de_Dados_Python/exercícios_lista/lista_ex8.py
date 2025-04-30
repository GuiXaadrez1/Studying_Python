# Escreva uma função que leia o arquivo words.txt e construa uma lista com um elemento
# por palavra. Escreva duas versões desta função, uma usando o método append e outra
# usando a expressão t = t + [x]. Qual leva mais tempo para ser executada? Por quê?

import os 

caminho_arq = os.path.join(os.getcwd(),'Estrutura_de_Dados_Python','exercícios','words.txt')

def reader_txt1(caminho):
    with open(caminho_arq,'r') as arq_lido:
        
        lista_construida = []
        for linha in arq_lido:
            elementos = linha.strip().split()
            for item in elementos:
                lista_construida.append(item)
        return lista_construida        

print(f'{reader_txt1(caminho_arq)}\n')
    
# convertendo em uma frasa completa de string
for i in reader_txt1(caminho_arq):
    print(i,end=' ')
    #print(type(i))    
    

def reader_txt2(caminho):
    with open(caminho_arq,'r') as arq_lido:
        
        lista_construida = []
        for linha in arq_lido:
            elementos = linha.strip().split()
            for item in elementos:
                lista_construida = lista_construida + [item]
        return lista_construida

print(f'\n\n{reader_txt2(caminho_arq)}')
    
'''
Duas versões foram escritas para ler palavras de um arquivo e adicioná-las a uma
lista: uma usando o método append() e outra usando t = t + [x]. A versão com append()
é mais eficiente porque modifica a lista em memória diretamente (O(1)),
enquanto t = t + [x] recria a lista a cada adição (O(n)), o que torna essa abordagem
significativamente mais lenta para grandes quantidades de dados.
'''