'''

Desempacotamento e Ignorar Itens

Dada a tupla coords = (10, 20, 30, 40, 50), desempacote os dois primeiros valores em x, y
e o restante em uma lista chamada resto.

Faça outro desempacotamento onde você só se interessa pelo primeiro e último valor
(ignore o meio).

'''

coords = (10, 20, 30, 40, 50)
# desempacotamento 1
resto = []
for i,item in enumerate(coords):  
    x,y = zip(coords[0:2])
    if i > 1:
        resto.append(item)    
print(f'\nDesempacotamento 1\ncoordenda x: {x[0]}\ncoordenada y: {y[0]}\nresto: {resto}')

# desempacotamento 2

lista_coordenadas = []
z = zip(coords)
for i,item in enumerate(z):
    lista_coordenadas.append(item)
    if i == 4:
        x = lista_coordenadas[0] # primeiro valor
        y = lista_coordenadas[4] # segundo valor        

print(f'\nDesempacotamento 2\ncoordenda x: {x[0]}\ncoordenada y: {y[0]}')