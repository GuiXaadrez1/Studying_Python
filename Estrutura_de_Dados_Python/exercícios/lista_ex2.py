'''
Escreva uma função chamada nested_sum que receba uma lista de listas de números inteiros
e adicione os elementos de todas as listas aninhadas. 
'''

t = [[1, 2], [3], [4, 5, 6]] # lista aninhada, lista dentor de lista

# criando a função que ira somar todos os números em cada item da lista
# função primeira versão
def nested_sum(lista:list):

    total = 0
    for i in lista:
        for num in i:
            total += num
    return total
            
print(f'Resultado final é:{nested_sum(t)}')
'''
Explicação da primeira versão
'''

print()
def nested_sumv2(lista: list):
    total = 0
    for row_index, row_data in enumerate(lista):
        for column_index, item in enumerate(row_data):
            total += item
    return total
print(f'Resultado final é:{nested_sumv2(t)}')
'''
Explciação da segunda versão
'''