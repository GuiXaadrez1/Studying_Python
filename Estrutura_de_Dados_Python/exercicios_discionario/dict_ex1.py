'''

Crie um dicionário pessoa com chaves "nome", "idade" e "cidade".

Acesse e imprima cada valor usando indexação direta (pessoa['nome']).

Tente acessar uma chave inexistente e trate o KeyError via try/except

'''

pessoa = {'nome':'Guilherme','idade':23,'cidade':'São Paulo'}

print(pessoa['nome']) # acessando diretamente os valores da chave nome

try:
    pessoa['carro']
except Exception as e:
    print('Infelizmente essa Chave não existe no nosso Dicionário de Dados')
    print('Tente novamente.')