'''
    Crie um código que mostre como funciona a comunicação coletiva do tipo broadcast 
    no MPI, usando mpi4py, onde um processo envia a mesma informação para todos os 
    outros processos.
'''

if __name__ == '__main__':
    
    from mpi4py import MPI
    
    comm = MPI.COMM_WORLD    
    worker = comm.Get_rank()
    size = comm.Get_size
    
    # se o trabalhador/rank for o 0
    if worker == 0:
      data = {"data":"for everyone","something":[1,2,3,4,5]}    
    # criar um dado, que é um dicionário
    else:
        data = None
    # realizando comunicação coletiva usando o brodcast
    # usando um método que faz isso
    # quem distribui via brodcast essa comunicação é o rank 0
    data = comm.bcast(data,root = 0)
    print(worker,data)
    
'''
    Broadcast (ou difusão) é um tipo de comunicação coletiva em 
    MPI (Message Passing Interface), onde um único processo (chamado de root) 
    envia a mesma mensagem para todos os outros processos do grupo.
'''