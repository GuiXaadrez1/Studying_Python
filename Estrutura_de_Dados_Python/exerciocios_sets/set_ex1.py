''' 
    Crie um set chamado frutas com os valores: 'maçã', 'banana', 'laranja', 'maçã'.

    Imprima o set e observe o que acontece com os valores duplicados.
    
    Verifique se 'banana' está no set frutas.

    Verifique se 'uva' está no set frutas.
    
    Adicione 'uva' ao set frutas.

    Remova 'maçã' do set.

    Tente remover 'abacaxi' de forma segura (sem erro).
    
    Imprima a quantidade de elementos no set frutas.

'''
frutas = {'Maçã','Banana','Laranja','Maçã','Banana','Laranja','Maçã'}

print(frutas) # {Maçã, Banana,Laranja}, percebe-se que os elementos duplicados deixa de existir

# Fazendoo a validação

print('Banana' in frutas) # True

print('Uva' in frutas) # False

# adcionando uva ao final do set
frutas.add('Uva')
print(frutas)

# Organizando por ordem alfabetica as fruas
print(sorted(frutas)) # organiza e retorna uma lista

frutas.remove('Maçã') # removendo a maçã
print(frutas)

# Tentando remover abacaxi de forma segura

try:
    frutas.remove('Abaxaxi')
except Exception as e:
    print('Não é possível remover a fruta, ela não exite no set.')

# imprindo a quantidade de elementos no set frutas
print(len(frutas)) # saida -> 3