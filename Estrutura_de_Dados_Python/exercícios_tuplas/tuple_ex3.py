#Defina uma tupla t = ('Maçã', 'Banana', 'Cereja', 'Damasco').
#Imprima o primeiro e o último elemento usando índices positivos e negativos.
#Acesse a sub-tupla que vai do segundo ao quarto elemento (inclusive).

t = ('Maçã', 'Banana', 'Cereja', 'Damasco')

print(t[0]) # primeiro elemento 
print(t[-1]) # segundo elemento

print('\n-------------\n')

sub_t = t[1:]

for item in sub_t:
    print(item)    
    