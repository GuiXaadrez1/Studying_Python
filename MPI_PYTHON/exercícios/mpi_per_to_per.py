'''

Criar uma cadeia de processos que passam uma mensagem de um para o outro, cada um
multiplicando o número por 2, até que o último mostre o resultado.

'''

if __name__ == "__main__":
    
    from mpi4py import MPI

    comm = MPI.COMM_WORLD 
    worker = comm.Get_rank()
    size = comm.Get_size()
    
    initial = 2 
    
    # Só o processo 0 entra aqui. Ele envia o número 2 para o processo 1
    if worker == 0:  # atenção ao bloco de código
        print(f'Tamanho do grupo MPI: {size}')
        
        comm.send(initial, dest=worker+1) 
        print(f'Processo {worker} enviou mensagem para o processo {worker+1}')
    
    # Último processo
    elif worker == size-1: 
        
        receber = comm.recv(source=worker-1) # recebe dados dos trabalhadores
        print(f'Processo {worker} multplicou a mensagem por 2 e o resultado final e: {receber*2}') 
  
    #  Processo 1 recebe e multiplica por 2, e envia para o 2
    else:
        receber = comm.recv(source=worker-1) 
        enviar = comm.send(receber*2, dest=worker+1)
        print(f'Processo {worker} recebeu mensagem {receber} do processo {worker - 1}')
        print(f'Processo {worker} multiplicou a mensagem por 2 e enviou para o processo {worker+1}')


'''

    Essa é uma forma de comunicação pont - to - pont ou também conhecida: ponto a ponto
    Comunicação ponto a ponto em MPI (Message Passing Interface) é o envio direto de
    mensagens entre dois processos específicos: um remetente e um destinatário, usando
    chamadas explícitas como send() e recv().

    Essa comunicação é determinística e exige que:

    O processo A saiba quem é o processo B (e vice-versa);

    Ambos estejam explicitamente preparados para enviar ou receber a mensagem

    O MPI, ao ser executado, inicia um conjunto de processos independentes, cada um com
    seu próprio rank (ID), dentro de um comunicador (por padrão, MPI.COMM_WORLD).
    Esses processos não compartilham memória, e a única forma de trocarem dados é por
    mensagens.

    Quando você usa send() e recv():

    Ciclo básico:
    O processo emissor executa comm.send(objeto, dest=rank_do_destino)

    O processo receptor executa comm.recv(source=rank_do_emissor)

    O MPI gerencia um canal de comunicação entre os dois, transmitindo os dados.

    Ambos os processos ficam bloqueados até que a troca se complete, garantindo sincronia.
'''