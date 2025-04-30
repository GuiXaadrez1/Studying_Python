# Escreva uma função chamada chop que tome uma lista alterando-a para remover 
# o primeiro e o último elementos, e retorne None.

t = [1, 2, 3, 4] 

def chop(lista:list) -> list:
    
    if len(lista) > 1:
        lista.pop(0)
        lista.pop(-1)

        return None
      
print(chop(t))
