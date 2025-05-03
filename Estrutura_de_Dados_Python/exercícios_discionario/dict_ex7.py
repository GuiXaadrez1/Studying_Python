'''

Crie uma agenda com buscas por nome e telefone, e permita edição e exclusão.

edição -> atualizar, consultar e inserir
'''

import sys

# dados MOC
agenda = [
    
    {
        'Nome':'Anna',
        'Telefone':'991543212'
    },
    {
        'Nome':'João',
        'Telefone':'991543712'
        
    },
    {
        
        'Nome':'Pedro',
        'Telefone':'997548213'             
    }
]

def buscar_por_nome(nome:str)->str: 
  
    for registro in agenda:
        if nome in registro.get('Nome'):
            return f"{nome} - {registro.get('Telefone')}"
        
def buscar_por_telefone(telefone:str)->str:
  
    for registro in agenda:
        if telefone in registro.get('Telefone'):
            return f"{registro.get('Nome')} - {telefone}"

def consultar_todos_nomes():
  
    for registro in agenda:
        print(registro.get('Nome'))

def consultar_todos_telefones():
  
    for registro in agenda:
        print(registro.get('Telefone'))

def consultar_todos_nomes_e_telefones():
    for registro in agenda:
        print('Nome - {}:Telefone - {}'.format(registro.get('Nome'),registro.get('Telefone')))

def inserir_nome_telefone(nome, telefone):

    new_registro = { 'Nome':nome, 'Telefone':telefone }
    agenda.append(new_registro)
    return '\nContato registrado com Sucesso!'

def atualizar_nome_telefone(nome,telefone):
    
    for index, registro in enumerate(agenda):
        
            if registro.get('Nome') == nome and registro.get('Telefone') == telefone:
        
                new_nome = input('\nDigite o novo nome: ')
                new_telefone = input('Digite o novo telefone: ')
                registro['Nome'] = new_nome
                registro['Telefone'] = new_telefone
                
                #print(f'Agenda atualizada com Sucesso!\n{agenda[index]}')
                return f'\nAgenda atualizada com Sucesso!\n{buscar_por_nome(new_nome)}'
        
            else:       
                return '\nNão foi possível achar esse contato!'
     
def deletar_nome_telefone(nome,telefone):
    
    for index, registro in enumerate(agenda):
        if registro.get('Nome') == nome and registro.get('Telefone') == telefone:
            agenda.pop(index)
            return f'\nNome e telefone deletado com Sucesso!'
        else:
            return'\nNão foi possível achar esse contato para deletar'

def coletar_nome():
    nome = input('\nDigite o nome do contato: ')
    return nome

def coletar_telefone():
    telefone = input('Digite o telefone do contato: ')
    return telefone

def questionar():
    while True:
        
        resposta = input('\nDeseja fechar programa? (sim ou não): ')
        if resposta.lower() == 'sim':
            return True
        
        if resposta.lower() != 'não':
            print('Tente novamente')
        
        else:
            return False
        

def fechar_programa(resposta):
    
    if resposta == True:
       print('\nPrograma Finalizado!')
       sys.exit(-1) 
        
if __name__ == '__main__':
    
    while True: 
        
        print('''\n
            Ações que você pode fazer no sistema:\n
            [1] Buscar contato pelo nome
            [2] Buscar contato pelo telefone
            [3] Consultar somente todos os nomes
            [4] Consultar somente todos os telefones
            [5] Consultar todos os nomes e seus telefones
            [6] Inserir novo contato
            [7] Atualizar contato 
            [8] Deletar contato
            [9] Finalizar Programa
            \n''')
        
        funcionalidade = int(input('Escolha um número para realizar ação desejada: '))
            
        if funcionalidade == 1:
            
            nome = coletar_nome()
            print(buscar_por_nome(nome))
            resposta = questionar()
            fechar_programa(resposta)
            
        elif funcionalidade == 2:
        
            telefone = coletar_telefone()
            print(buscar_por_telefone(telefone))
            resposta = questionar()
            fechar_programa(resposta)
        
        elif funcionalidade == 3:
            
            consultar_todos_nomes()
            resposta = questionar()
            fechar_programa(resposta)
            
        elif funcionalidade == 4:
            consultar_todos_telefones()
            resposta = questionar()
            fechar_programa(resposta)
        
        elif funcionalidade == 5:
            
            consultar_todos_nomes_e_telefones()
            resposta = questionar()
            fechar_programa(resposta)
        
        elif funcionalidade == 6:
            
            nome = coletar_nome()
            telefone = coletar_telefone()
            
            print(inserir_nome_telefone(nome,telefone))
            resposta = questionar()
            fechar_programa(resposta)
            
        
        elif funcionalidade == 7:
            
            nome = coletar_nome()
            telefone = coletar_telefone()
            
            print(atualizar_nome_telefone(nome,telefone))
            resposta = questionar()
            fechar_programa(resposta)
        
        elif funcionalidade == 8:
            nome = coletar_nome()
            telefone = coletar_telefone()
            
            print(deletar_nome_telefone(nome,telefone))
            resposta = questionar()
            fechar_programa(resposta)
        
        elif funcionalidade == 9:
            
            resposta = questionar()
            fechar_programa(resposta)
            
        else:
            print('\nNão existe essa funcionalidade disponível')