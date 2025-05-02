'''

Dada a string s = "python", converta-a em tupla de caracteres.

A partir de lista = [10, 20, 30], crie uma tupla equivalente, modifique a lista e mostre
que a tupla não sofre alterações.

Explique, em comentários no código, por que a conversão é útil para garantir
imutabilidade.

'''

s = "python"

print(tuple(s)) # criando uma tupla de caracteres

lista = [10, 20, 30]  

tuple = (10,20,30) # a tupla não será modificada já a lista sim

for i in range(1,101):
    lista.append(i)

print(lista) # a lista teve os seus valores alterados, pois é característica possuir essa flexibilidade

print(tuple) # a tupla permanece imutável pois está em um espaço da memória ram diferente
# ela não pode ter valores mudados um vez que foii definidos