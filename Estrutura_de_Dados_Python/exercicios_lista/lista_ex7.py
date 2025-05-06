# Escreva uma função chamada has_duplicates que tome uma lista e retorne True se houver
# algum elemento que apareça mais de uma vez. Ela não deve modificar a lista original.

t = ['a','b','c','a']
t1 = ['a','b','c','d','e']

def has_duplicates(lista:list)->bool: # a saida deve ser um True
    
    print(len(lista)) # saida -> 4
    print(len(set(lista))) # sida -> 3
        
    return len(lista) != len(set(lista)) # comparamoso tamnho daa lista com o set

print(has_duplicates(t))
print(has_duplicates(t1))

'''

Explicação do código: Os conjuntos em Python não permitem elementos duplicados. 
Você pode comparar o tamanho da lista original com o tamanho do conjunto criado 
a partir da lista. Basicamente convertemos a nossa lista em um set, o set não aceita dados
duplicados, com isso comparamos o tamnho da lista com a função len() e retornamos True 
ou False.

'''