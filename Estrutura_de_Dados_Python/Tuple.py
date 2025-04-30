# Vamos reaprender e reforçar o conteudo a respeito da tupla

# criando uma tupla  de números
tupla = (1,2,3,4,5)

print(type(tupla)) # <class 'tuple'

# um único elemento string dentro da de uma tupla não é tupla
tupla_string = ('a')
print(type(tupla_string)) # saida -> <class 'str'>

# agora se eu colocar duas strings aí sim vira uma tupla
tupla_string = ('a','b')
print(type(tupla_string)) # saida -> <class 'tuple'>

# ATRIBUIÇÕES EM TUPLAS

# Realizando multiplas atribuições 
#tupla_3 = ('arroz',1,'feijão')

tupla_1 = tupla
#tupla_string = tupla_3
#tupla_1 = tupla_3

#print(f'\nSolução trabalhosa de atribuição multipla de tuplas\nTupla_1:{tupla_1}\nTupla_String:{tupla_string}\nTupla_3:{tupla_3}')
#print("\nVeja que eu troquei o valor de cada tupla, atribuir uma tupla a outra.\nEntão isso se chama atribuição multipla.")

# forma elegante e pythonica de atribuição multipla
tupla_1, tupla_string = tupla_string, tupla_1
print(f'\nEssa é a forma pythonica de atribuição multipla. Veja!\nElementos da Tupla_1: {tupla_1}\nElementos da Tupla_String: {tupla_string}')

# CONCATENAÇÃO DE TUPLAS

tuplas_concatenadas = tupla_1 + tupla_string + (40,50)
print(f'\nO + concatena as tuplas: {tuplas_concatenadas}')