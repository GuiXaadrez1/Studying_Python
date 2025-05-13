'''

    Disparar valores

    Processo 0 envia diferentes números para os demais (com send/recv) e cada um imprime
    o valor rescebido

'''
from mpi4py import MPI
import random


def num_aleatório()->int:
    
    gerar_num = random.randint(0,100)
    
    return gerar_num

if __name__ == '__main__':
    
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    
    if rank == 0:
        
        lista_processos = []
        for processos in range(1,size):  
            comm.send(num_aleatório(),processos)
            lista_processos.append(processos)
        
        #print('Lista de processos' + str(lista_processos))
    
    elif rank != 0:
       
       resceber = comm.recv(source=0)
       print(f'Processo de numero {rank}, rescebeu o numero:{resceber} do processo 0')
    
        
    