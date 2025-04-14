# Escreva uma função chamada is_sorted que tome uma lista como parâmetro e retorne 
# True se a lista estiver classificada em ordem ascendente, e False se não for o caso. 

# ordem ascendente do maior para o menor
t = [1,2,3,4]

def is_sorted(lista: list) -> bool: # retorna um boelano True ou false
    for i in range(len(lista) - 1): # vamos pegar o numero total de elementos e subtrair um, funciona como se fosse (0,3) so que por index    
        if lista[i] > lista[i + 1]: 
            return False
    return True

t = [1, 2, 3, 4]
print(is_sorted(t))  # Resultado: True


# forma pytonica de resolver
def is_sorted(lista: list) -> bool:
    return lista == sorted(lista)
