'''

Insira uma nova chave "email" em pessoa.

Atualize "idade" somando mais 1 ao valor atual.

Use get() para ler uma chave "telefone" com valor default "não informado".

'''

pessoa = {'nome':'Guilherme','idade':23,'cidade':'São Paulo'}

pessoa['idade'] = pessoa['idade'] + 1

pessoa.update({'Email':'GuilhermeX1delas@13.gmail.com'})

print(pessoa)

print(pessoa.get('Telefone','Telefone não informado'))