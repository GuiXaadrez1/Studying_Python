'''

Remova "cidade" usando pop() e guarde o valor numa variável.

Remova "email" usando del.

Limpe todo o dicionário com clear() e verifique len(pessoa) == 0

'''

# Craindo e Inserindo Novos valores

pessoa = {'nome':'Guilherme','idade':23,'cidade':'São Paulo'}

pessoa['idade'] = pessoa['idade'] + 1

pessoa.update({'Email':'GuilhermeX1delas@13.gmail.com'})

print(pessoa)

print(pessoa.get('Telefone','Telefone não informado'))

# Removendo

removendo = pessoa.pop('cidade')

print(removendo) # São Paulo

del(pessoa['Email'])

print(pessoa)

pessoa.clear() # limpando todos os registros(valores) do dicionário

print(pessoa.clear())

if len(pessoa) == 0:
    print(True)
else:
    print(False)