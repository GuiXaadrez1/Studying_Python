from mpi4py import MPI
import os
import time

def somador(comm, caminho):
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    num_workers = size - 1  # Excluindo o coordenador (rank 0)
    
    start_time = time.time()
    if rank == 0:
        # Coordenador: ler o arquivo linha a linha e distribuir
        with open(caminho, 'r') as f:
            worker_rank = 1
            for linha in f:
                numero = int(linha.strip())
                comm.send(numero, dest=worker_rank)
                worker_rank += 1
                if worker_rank > num_workers:
                    worker_rank = 1
        
        # Enviar sinal de término para os workers
        for worker_rank in range(1, size):
            comm.send(None, dest=worker_rank)

        # Receber as somas parciais
        soma_total = 0
        for worker_rank in range(1, size):
            soma_parcial = comm.recv(source=worker_rank)
            print(f"Recebido soma {soma_parcial} do trabalhador {worker_rank}")
            soma_total += soma_parcial
        
        end_time = time.time()
        real_time = end_time - start_time
        
        print(f"\nSoma total final: {soma_total}")
        print(f"Tempo de execução: {real_time:.4f} segundos")

    else:
        # Cada trabalhador recebe números e calcula a soma incremental
        soma_local = 0
        while True:
            numero = comm.recv(source=0)
            if numero is None:
                break
            soma_local += numero
        print(f"Rank {rank} somou {soma_local}")
        comm.send(soma_local, dest=0)

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        caminho = os.path.join(os.getcwd(), 'saida2.txt')
        somador(comm, caminho)
    else:
        somador(comm, None)

if __name__ == "__main__":
    main()
