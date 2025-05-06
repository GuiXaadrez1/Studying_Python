'''

Operações com Dois Sets:

Dado:

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

Calcule:

A união

A interseção

A diferença A - B

A diferença simétrica

Conversão entre tipos:

Dado o seguinte list com valores duplicados:

nomes = ['Ana', 'João', 'Maria', 'João', 'Ana']

Elimine os duplicados usando um set e converta de volta para list.

Set comprehension:

Crie um set com todos os quadrados perfeitos entre 1 e 100 usando set comprehension.

'''



def calculos(set1,set2):
    print(f'A união: {set1 | set2}') # união
    print(f'A interseção: {set1 & set2}') # interseção 
    print(f'A diferença: {set1 - set2}') # diferença
    print(f'A diferença simêtrica: {set1 ^ set2}\n') # diferença simêtrica


def remover_duplicados(lista:list)->set:
    """ Rescebe uma lista com dados duplicados

    Args:
        lista (list): lista com dados duplicados

    Returns:
        new_lista -> lista sem dados duplicados
    """
    lista_old = set(lista)
    new_lista = list(lista_old)
    
    return new_lista

def lista_num(inicio, final)->list:
    count = []
    for numeros in range(inicio, final+1):        
        count.append(numeros)
    return count

def quadrado_perfeito(numeros: list) -> set:
    quadrados = {x**2 for x in numeros}  # Aqui a função recebe uma lista como argumento
    return quadrados

if __name__ == '__main__':
    
    # dados par ao calculo
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    calculos(A,B)
    
    # Lista com valores duplicados
    nomes = ['Ana', 'João', 'Maria', 'João', 'Ana']
    print(remover_duplicados(nomes))
   
    # fazendo uma lista numeros  
    numeros = lista_num(1,100)
    
    quadrados = (quadrado_perfeito(numeros))
    
    lista_quadrados = []
    for elemento in sorted(quadrados):
        lista_quadrados.append(elemento)

    print(lista_quadrados)        
   
