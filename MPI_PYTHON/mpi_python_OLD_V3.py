from mpi4py import MPI
import os
import time

def read_txt(nome: str):
    with open(nome, 'r') as f:
        linhas = f.readlines()
    numeros = [int(l.strip()) for l in linhas]  # list comprehension
    return numeros

def somador(comm, numeros):
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    num_workers = size - 1  # Excluindo o coordenador (rank 0)
    
    start_time = time.time()
    if rank == 0:
        # Dividir os números para os trabalhadores
        n = len(numeros)
        chunk_size = n // num_workers
        extras = n % num_workers  # para distribuir os restos

        inicio = 0
        for worker_rank in range(1, size):
            fim = inicio + chunk_size + (1 if worker_rank <= extras else 0)
            sublista = numeros[inicio:fim]
            comm.send(sublista, dest=worker_rank)
            inicio = fim
        
        # Receber as somas parciais
        soma_total = 0
        for worker_rank in range(1, size):
            soma_parcial = comm.recv(source=worker_rank)
            print(f"Recebido soma {soma_parcial} do trabalhador {worker_rank}")
            soma_total += soma_parcial
        
        end_time = time.time()
        real_time = end_time - start_time
        
        
        print(f"Soma total final: {soma_total}")
        print(f"Tempo de execução:{real_time}")

    else:
        # Cada trabalhador recebe uma sublista e calcula a soma
        sublista = comm.recv(source=0)
        soma_local = sum(sublista)
        print(f"Rank {rank} somou {soma_local} a partir de {sublista}")
        comm.send(soma_local, dest=0)

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        caminho = os.path.join(os.getcwd(), 'saida3.txt')
        reader = read_txt(caminho)
        somador(comm, reader)
    else:
        somador(comm, None)

if __name__ == "__main__":
    main()
