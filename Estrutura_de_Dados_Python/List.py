# Vamos nos aperfeiçoar sobre estrutura de dados com python
# O objetivo é reaprender e reforçar o conteudo

# Criando uma lista

lista = ['a','b','c','d','e'] # lista de strings
print(type(lista)) # <class 'list'>

# puxando o elemento de index 4, com o slice

print(lista[4]) #saida e 

print(lista[-2])# saida d o penultimo

# listas são ordenadas e mutáveis

lista1 = lista # estamos apontando essas duas variáveis para mesmo endereço de memória, neste caso não criamos uma nova lista

lista1[0]=100 # mudando o valor do elemento na posiçãp index de número 0 para 100

print(f'\n{lista1}') 

print(lista1 == lista) # saida True, então neste caso as duas variáveis apontam para o mesmo endereço de memória

print(id(lista)) # saida 2047423713536 endereço de memória com um identificador no meu caso
print(id(lista1)) # saida 2047423713536 endereço de memória com um identificador no meu caso

# vendo o endereço de memória no formato de máquina hexadecimal

print(hex(id(lista))) # saida 0x1d4c6639100 no meu caso
print(hex(id(lista1))) # saida 0x1d4c6639100 no meu caso

# invertendo a lista1 rapidamente
print(lista1[::-1]) # invertemos foi tudo


# avançando cada elemento da lista1 a cada dois elementos
# lista[início:fim:passo] veja como funciona o slicing
print(lista1[::2])
# neste caso começamos no index 0 e passamos de 2 em duas casas

# usando alguns métodos de manipulação para listas
lista1.append(50) # adiciona o elemento ao final da lista
print(lista1)

lista1.remove('c')# remove o primeiro c que encontrar
print(lista1)

print(len(lista1))# vai mostrar a quantidade de elementos que existem na lista1

lista1.insert(3,'ab')# na posição de index 3, vamos sobescrever ab
print(lista1)

lista1.pop(2)# remover o elemento dois da lista, se não passar parametros, retorna o último item da lista
print(lista1)
print(lista1.pop()) # devolve o ultimo elemento da lista

print(lista1.index(100))# vai retornar o index da primeira ocorrência

lista1.reverse()#inverte a ordem da lista
print(lista1)

lista[-1]='abc'
lista1.sort()# vai ordenar a lista em ordem sequêncial neste caso, alfabetica
print(lista1)

print(lista.count('abc'))# irá contar quantas vezes aquele elemento aparece na lista

nova_lista1 = lista1.copy()# realiza a cópia da lista1 que será armazenada em outro endereço de memória
print(hex(id(nova_lista1)))# veja que 0x2753aa28780 != 0x1d4c6639100 no meu caso

lista1.clear()# basicamente vai resetar nossa lista, torna ela vazia.
print(lista1)# saida []

lista_num =[1,2,3,4,5,6,7,8,9,10] # criando uma lista de números

#interação básica na lista com tomada de decisão
num_par = [] # definindo uma lista vazia
for i in lista_num: 
    if i % 2 == 0:
        num_par.append(i) # adcionando o número par ao final da lista

print(f'lista de número pares:{num_par}')   


# juntando listas

lista_a =  ['a','b','c']
lista_b = ['1','2','3']

listas_juntas = lista_a + lista_b #concatenei
print(listas_juntas)

# realizando uma operação matemática entre duas listas
lista_num1 = [1, 2, 3, 4]
lista_num2 = [5, 6, 7, 8]

# Usando zip() para somar elemento a elemento
lista_somada = [a + b for a, b in zip(lista_num1, lista_num2)]
print(lista_somada)

