# Escreva uma função chamada cumsum que receba uma lista de números e retorne a soma
# cumulativa; isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 
# elementos da lista original.

t = [1, 2, 3]

def cumsum(lista:list):
    
    cont = 0
    lista_num = []
    for i in lista:
        
        cont += i
        lista_num.append(cont) 
    
    return f'O resultado deu: {lista_num}'

print(cumsum(t))