from mpi4py import MPI 
import os
import time

def read_txt(nome: str):
    with open(nome, 'r') as f:
        linhas = f.readlines()
    numeros = [int(l.strip()) for l in linhas] # list compression
    print(type(numeros))
    return numeros

def somador(comm,reader):
    rank = comm.Get_rank() # identificando os processos do MPI, lembrando que são idenpendentes
    size = comm.Get_size() # quantidade total de processos, (comunicador e trabalhadores)
    
    if rank == 0:
        numeros = reader # números a serem somados
        num_workers = size - 1 # acabamos de definir a quantidade de trabalhadores menos o comunicador

        comm.send(numeros)
        




    
    print(f'Quantidade de trabalhadores: {num_workers}') # total de processos menos o comunicador
    

def main():
    print("Inicializado o MPI",flush=True)
    
    comm = MPI.COMM_WORLD # inicializa o ambiente MPI.
    rank = comm.Get_rank() # identificando os processos do MPI, lembrando que são idenpendentes
    
        
    if rank == 0: # comunicador(coordenador)
        caminho = os.path.join(os.getcwd(), 'somarnum.txt')
        reader = read_txt(caminho)
        
        print(reader) # retonra a lista de numeros
        
        somador(comm,reader)
    
    else:
        reader = None

if __name__ == "__main__":
    test = main()
