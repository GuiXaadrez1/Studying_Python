from mpi4py import MPI
import numpy as np
import os


def read_txt_as_numpy(filename: str):
    with open(filename, 'r') as f:
        text = f.read()
    numbers = np.fromstring(text, sep=' ', dtype=np.int64)
    
    print(numbers)
    return numbers

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Começa a medir o tempo de execução real
    total_start_time = MPI.Wtime()

    if rank == 0:
        caminho = os.path.join(os.getcwd(), 'saida3.txt')
        numeros = read_txt_as_numpy(caminho)

        n = len(numeros)
        counts = np.full(size, n // size, dtype=int)
        counts[:n % size] += 1  # distribui o resto
        displs = np.insert(np.cumsum(counts), 0, 0)[0:-1]  # deslocamentos
        
    else:
        numeros = None
        counts = None
        displs = None

    # Broadcast do tamanho de cada pedaço para todos
    counts = comm.bcast(counts, root=0)

    # Cada processo cria um array local para receber seus dados
    local_numeros = np.zeros(counts[rank], dtype=np.int64)

    # Distribui os dados (scatterv = tamanhos variáveis)
    comm.Scatterv([numeros, counts, displs, MPI.LONG], local_numeros, root=0)

    # Cada processo calcula sua soma local
    local_sum = np.sum(local_numeros)

    # Reduz (soma) todas as somas locais no mestre
    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

    # Termina a medida do tempo
    total_end_time = MPI.Wtime()
    total_time = total_end_time - total_start_time

    if rank == 0:
        print(f"\n===== Resultados =====")
        print(f"Resultado final da soma: {total_sum}")
        print(f"Tempo total de execução: {total_time:.6f} segundos")
        
        # Para calcular speedup e eficiência, precisamos de tempo sequencial
        # Idealmente, mediríamos o tempo de execução com 1 processo!
        # Vamos assumir (temporariamente) que você mediu esse tempo e substitui aqui:
        tempo_sequencial = 0.3  # EXEMPLO -> você deve medir rodando com 1 processo

        speedup = tempo_sequencial / total_time
        eficiencia = (speedup / size) * 100

        print(f"Speedup: {speedup:.2f}x")
        print(f"Eficiência: {eficiencia:.2f}%")
        print(f"======================\n")

if __name__ == "__main__":
    main()
