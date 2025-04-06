from mpi4py import MPI 

'''
 quantidade de ranks não é definida dentro do seu código Python.

 Ela é definida na hora de executar o script, usando o comando mpiexec ou mpirun,
 com o parâmetro -n (ou --np).
'''

def main():
    # definindo o comunicador principal
    comm = MPI.COMM_WORLD # inclui todos os processos definidos pelo usuário numa aplicação MPI 
    total_process = comm.Get_size()# retorna o número total de processos no comunicador
    
    rank = comm.Get_rank() # adquire a quantidade de ranks no comunicador

    if MPI.COMM_WORLD.Get_size() < 4:
        print("Poucos processos! Recomendo usar pelo menos 4.")
         
    return f'Existem {total_process} raks no comunicador, esse e o rank de id(processo): {rank}'

if __name__ == "__main__":

    test = main()
    print(test)
