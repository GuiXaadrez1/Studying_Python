'''

Com a tupla cores = ('azul', 'verde', 'azul', 'amarelo', 'azul'), determine quantas
vezes 'azul' aparece e em que posição ele aparece pela primeira vez.

O que acontece se você chamar index com um valor que não existe? Teste e trate essa
situação com try/except.

'''

cores = ('azul', 'verde', 'azul', 'amarelo', 'azul')

try:
    for i,item in enumerate(cores):
        
        resultado = cores.count('azul'), cores.index('azul')
        # rultado é uma variável que armazena uma tupla
        # contendo os valores de qunatas vezes a cor azul é repetida
        # e quando ela aparece pela primeira vez
    
    print(f'Aparecem {resultado[0]} vezes o azul na tupla\nAparece azul pela primeira vez no index: {resultado[1]}')

    cores.index(5) # erro propocital para usar try e execpt
    
except Exception as e:
    print(f'Aconteceu alguma cagada aqui {e}')
    
    