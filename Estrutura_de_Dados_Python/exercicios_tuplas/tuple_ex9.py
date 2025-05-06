'''

Escreva uma função swap(t, i, j) que receba uma tupla t e dois índices i, j e 
retorne uma nova tupla onde os valores nas posições i e j foram trocados.

Exemplo: swap((10,20,30,40), 1, 3) deve retornar (10, 40, 30, 20).

'''

# Fazendo a função da maneira mais fácil, usando lista

def swap(t,i,j) -> tuple:
    """

    Args:
        t (tupla): _description_
        j (index): _description_
        i (index): _description_
    
    """
    
    # Converte tupla em lista
    lst = list(t)
    
    # Troca os itens nas posições i e j
    lst[i], lst[j] = lst[j], lst[i]
    
    # Retorna uma nova tupla
    return tuple(lst)

tupla1 = (10,20,30,40,50,60,70,80,90,100)

print(swap(tupla1,5,8))


# Fazendo da maneira mais difícil, usando apenas tuplas, aqui usei o chatgpt 

def swap(t: tuple, i: int, j: int) -> tuple:
    
    # Garante que i < j para simplificar os slices
    if i > j:
        i, j = j, i

    # Partes antes de i
    left  = t[:i]
    
    # Elemento j vai para a posição i
    mid1  = (t[j],)
    
    # Elementos entre i+1 e j-1
    middle = t[i+1:j]
    
    # Elemento i vai para a posição j
    mid2  = (t[i],)
    
    # Partes depois de j
    right = t[j+1:]

    # Concatena tudo em nova tupla
    return left + mid1 + middle + mid2 + right

print(swap((10, 20, 30, 40), 1, 3))

'''
left = t[:i]

    Pega todos os elementos antes de i.

    Slice t[:i] vai do índice 0 até i-1.
    
    left = (10,)


mid1 = (t[j],)

    Cria uma tupla de um único elemento contendo o valor que estava em j.

    Esse valor vai ocupar a posição i na tupla resultante.
    
    mid1 = (40,)

middle = t[i+1:j]

    Pega o intervalo “entre” i e j, sem incluir nenhum dos dois.

    Slice t[i+1:j] vai de i+1 até j-1
    
    t[2:3]  # índice 2 até 2 → (30,)

mid2 = (t[i],)
    
    Cria uma tupla de um elemento com o valor que estava em i.
    
    Esse valor vai ocupar a posição j na nova tupla.

    mid2 = (20,)
    
right = t[j+1:]

    Pega tudo que vem depois de j.

    Slice t[j+1:] começa em j+1 e vai até o fim.

    Se j = 3, então t[4:] no exemplo original (t com 4 elementos) é vazio:
    
    right = ()

    mas em tuplas maiores, incluiria os elementos seguintes

Concatenação Final:
    
    left   = (10,)
    mid1   = (40,)
    middle = (30,)
    mid2   = (20,)
    right  = ()


    return left + mid1 + middle + mid2 + right

'''