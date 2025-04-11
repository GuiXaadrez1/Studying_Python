from mpi4py import MPI 
import os

# essa função ira resceber o nome do arquivo.txt que será lido para somar cada linha
def read_txt(nome: str):
    with open(nome, 'r') as f:
        linhas = f.readlines()
    numeros = [int(l.strip()) for l in linhas]
    return numeros

def dist_sum(comm, reader):
    rank = comm.Get_rank() # numero do processo MPI
    size = comm.Get_size() # quantidade de processos no nosso MPI

    if rank == 0:
        numeros = reader # números a serem lidos
        num_workers = size - 1 # 4 trabalhadore menos um é o comunicador todos os processos.

        while len(numeros) > 1:
            workers_in_use = min(num_workers, len(numeros)//2)

            for worker_id in range(1, workers_in_use + 1):
                n1 = numeros.pop(0)
                n2 = numeros.pop(0)
                comm.send((n1, n2), dest=worker_id, tag=11)
            
            for worker_id in range(1, workers_in_use + 1):
                soma = comm.recv(source=worker_id, tag=22)
                numeros.append(soma)

        for worker_id in range(1, size):
            comm.send(None, dest=worker_id, tag=99)

        print(f"Resultado final da soma: {numeros[0]}")

    else:
        while True:
            status = MPI.Status()
            dados = comm.recv(source=0, tag=MPI.ANY_TAG, status=status)
            if status.Get_tag() == 99:
                break

            n1, n2 = dados
            resultado = n1 + n2
            comm.send(resultado, dest=0, tag=22)


def main():
    comm = MPI.COMM_WORLD
    total_process = comm.Get_size()
    rank = comm.Get_rank()

    if total_process < 4 and rank == 0:
        print("Poucos processos! Recomendo usar pelo menos 4.")
    
    if rank == 0:
        caminho = os.path.join(os.getcwd(), 'somarnum.txt')
        
        reader = read_txt(caminho)
    else:
        reader = None
    
    dist_sum(comm, reader)

    return f'Existem {total_process} ranks no comunicador, este é o rank de id(processo): {rank}'

if __name__ == "__main__":
    test = main()
    print(test)
