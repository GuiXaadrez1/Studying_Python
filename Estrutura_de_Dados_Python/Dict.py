# Vamos rever alguns conceitos do dicionário em python

# criando dicionário da forma tradicional {chave:valor}
dict1 = {'Status':[True,True,False,True,False],'Vendas':'Macarrão'}
#print(dict1)

# criando dicionário através do construtor
dict2 = dict(status=True,jogador='GuiDelas123')

# acessando um item no dicionário

print(dict1.get('Status'))
print(dict1['Vendas'])

# Atribuindo ou atualizando dicionários

dict1['Status'].append(True) # aqui atualizamos uma valor da lista na chave Status
print(dict1)


