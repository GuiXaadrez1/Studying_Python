# Escreva uma função chamada middle que receba uma lista e retorne uma nova lista com todos
# os elementos originais, exceto os primeiros e os últimos elementos.

t = [1, 2, 3, 4] 

# O -> é parte da anotação de tipo de retorno de uma função, também chamada de "type hint"
# (dica de tipo).

def middle(lista:list) -> list:
    lista.pop(0),lista.pop(-1)     
    return f' O resultado deu: {lista}'
print(middle(t))
        