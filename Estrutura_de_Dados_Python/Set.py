# Aqui vamos revisar Sets

# criando um set, lembrando que ele possui valores unicos e permite duplicatas
# é como se fosse criar um dicionário, porém sem chave e valores

set1 = {1,2,3,4,5,6,7,8,9,10} # criando um set de inteiros
print(type(set1)) 

# concatenando set

set2 = {1.2,1.3,1.4,1.5}

sets_concatenados = set1 | set2 # usando conceito de união
print(sets_concatenados)

# ele elimina dulicadas, pois não aceita duplicadas
# com base em outras estruturas também podemos criar sets
# exemplo:

lista = ['a','b','b','c','c','c']
set3 = set(lista) # craindo set apartir de um método

# interando sobre os itens de set

for item in set3:
    print(item, end=''.replace('',';'))
