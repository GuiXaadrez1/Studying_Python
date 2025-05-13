'''

    Ping-pong

        Dois processos trocam uma mensagem várias vezes, contando 
        quantas vezes foi trocada.

'''

from mpi4py import MPI

comm = MPI.COMM_WORLD # criando canal de comunicação principal entre processos
size = comm.Get_size() # Qunatidade de processos dentro do canal principal
workers = comm.Get_rank() # puxando id de identificação dos processos

mensagem = 0         
contagem = 0
for i in range(0,10):
    
    if workers == 0:
       enviar = comm.send(mensagem,dest=workers+1) 
       receber = comm.recv(source=1)
       #print(f'Rank/trabalhador: {workers} recebeu de volta a mensagem: {mensagem}')
    elif workers == 1: 
        receber = comm.recv()
        print('Processo 1, recebeu a mensagem do processo 0')
        enviar = comm.send(mensagem,dest=0)
        print('Processo 1 enviou a mensagem de volta para o processo 0')   
    contagem += 1 

if workers == 1:
    print('Foram trocadas: %d mensagens entre os dois processos'%(contagem))       
 

exit()