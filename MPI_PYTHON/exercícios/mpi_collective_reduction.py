'''

    Crie um código que demonstre como funciona o reduction

    Objetivo:
        Mostrar como vários processos podem combinar seus dados em um único valor,
        usando uma função de redução personalizada (neste caso, soma).
        
        lembre-se: o processo de rank 0 participa da operação reduce como qualquer outro.

'''

if __name__ == '__main__':
    
    from mpi4py import MPI
   
    def reduce_func(a,b):
       return a + b # Define a operação de redução: soma
    
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    workers = comm.Get_rank()
    
    data = comm.reduce(workers,op = reduce_func,root=0)
    
    '''
        
        workers: é o valor que cada processo envia.

        op=reduce_func: é a função que será usada para agregar os dados (soma).

        root=0: é o processo que receberá o resultado final.
        
    '''
    
    print(workers,workers)
    
    if workers == 0:
        print("final result ", data)
    
    
    '''
        Conclusão:
            Esse código mostra como usar a comunicação coletiva com redução personalizada,
            onde vários processos cooperam para computar um único valor agregado,
            retornado ao processo raiz.
    '''    
   