import string

'''

Dado um texto, conte a frequência de cada palavra e armazene no dicionário.

'''

texto = "a ab abc abcd a b a abc def gh iop put ibput gh hg"

palavras = texto.split() # retornando uma lista de string
tuple(palavras) # convertendo para uma tupla

freq = {} # criando dicionário vazio 
for palavra in palavras: # atualizar o dicionário colocando a palavra e a frequência que ela aparece no texto
    freq.update({palavra:palavras.count(palavra)})

for chave,valor in freq.items():
    print(f'Frequência da palavra {chave}: {valor}')
    


