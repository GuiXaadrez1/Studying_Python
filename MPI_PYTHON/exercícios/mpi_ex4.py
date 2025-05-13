'''

    Reduce com Soma
        Cada processo gera um número. Use reduce para somar todos no rank 0.

'''

from mpi4py import MPI
import random
import time

def num_aleatório()->list:
    
    lista_num = []
    for i in range(0,10):
        gerar = random.randint(0,100)
        lista_num.append(gerar)
    
    return lista_num


def somar_lista(lista:int)->int:
    
    return sum(lista)


if __name__ == '__main__':
    
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    if rank != 0:       
        creat_list_num = num_aleatório()
        print(f'O rank {rank} gerou essa lista de números: {creat_list_num}')
        valor_local = somar_lista(creat_list_num)
    else:
        valor_local = 0  # rank 0 não contribui para a soma
    
      # todos os processos chamam reduce
    dados = comm.reduce(valor_local, op=MPI.SUM, root=0)
    
    if rank == 0:
        time.sleep(2)       
        print("Resultado final da soma de todos os processos:", dados)

    