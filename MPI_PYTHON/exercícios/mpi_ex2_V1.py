'''

    Disparar valores

    Processo 0 envia diferentes números para os demais (com send/recv) e cada um imprime
    o valor rescebido

'''
from mpi4py import MPI
import random


def num_aleatório(size_mpi)->list:
    
    lista_num = []
    for i in range(0,size_mpi):
        gerar = random.randint(0,100)
        lista_num.append(gerar)
    
    return lista_num

if __name__ == '__main__':
    
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    
    
    # trabalhador zero cria uma lista de 10 números aleatórios
    if rank == 0:
        list_num = num_aleatório(size) 
    else:
        
        list_num = None    
    #for ranks in range(0,size):
    data = comm.scatter(list_num,root=0)
    
    if rank != 0:
        print(f' processo de id {rank}, recebeu numero: {data}, do processo 0')
           