'''

    Crie um código que mostre como funciona o gather na comunicação coletiva de processos 
    no mpi
    
    Objetivo:
        Demonstrar como funciona a comunicação coletiva gather no MPI usando mpi4py 
        em Python.

'''

if __name__ == '__main__':
   from mpi4py import MPI
   
   comm = MPI.COMM_WORLD 
   size = comm.Get_size()
   workers = comm.Get_rank() # identificador do processo, conhecido como rank
   #print(type(worker)) # retorna um inteiro
   
   # os dados que os proceeos enviam para o root no caso o rank 0 
   data = comm.gather(workers**3,root = 0)
   # são o inteiro do seu próprio rank elevado ao cubo
   # exemplo: rank 1 processa 1 * 3 -> 1, o rank 2 processa 2 * 3 -> 8 
   
   print(f'Trabalhador: {workers}, processou seu rank ao cubo, resultado: {workers**3}')
   
   if workers == 0:
       print("final result ", data)
       print(type(data)) # o gather retorna uma lista
       
       # aqui retorna o resultado final para o rank 0, retornando  um lista
       # contendo o seguinte dado: o id, rank dos outros trabalhadores
       # elevado ao cubo

'''
    Explicação:
        A função gather é usada quando vários processos enviam dados para um processo
        central (geralmente o rank 0), que então reúne todos esses dados em uma lista.
'''