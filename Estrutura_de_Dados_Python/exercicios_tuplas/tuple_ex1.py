# Descompate com a função zip esses pares de tuplas em uma lista

pares = [(1, 'a'), (2, 'b')] # lista de tuplas

nums, letras = zip(*pares) # descompactar a lista de tuplas

print(nums,letras)
# veja que retorna duas tupla em variáveis diferentes, por conta da atribuição multipla

print(type(nums and letras)) # <class 'tuple'>

for i in nums,letras:
  ordenar = zip(nums,letras) # compactando novamente 

print(type(ordenar)) # zip

for item in ordenar:
  print(item) # puxando cada item dentro do zip