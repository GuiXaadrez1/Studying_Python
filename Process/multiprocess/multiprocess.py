# Vamos aprender sobre paralelismo com python...
# neste caso vamos aprender a usar com a biblioteca multiprocess 
# essa biblioteca basicamente

import time
import os
import sys
import multiprocessing
from multiprocessing import Process

# A função deve ficar no escopo global do módulo
def calcula_soma(numero:int=50000000):
    
    soma = 0 
    for i in range(numero):
        soma = soma + 1
        
    # Opcional: print para confirmar a execução de cada processo
    # print("Processo finalizou uma parte.")
    
    print(soma)

if __name__ == "__main__":
    
    start_time = time.time() 
    
    # Criamos os processos apontando para a função global
    
    # processo idepedente um
    codOne = multiprocessing.Process(target=calcula_soma)
    
    # processo idepedente dois
    codTwo = multiprocessing.Process(target=calcula_soma)
    
    # Inicia a execução
    codOne.start()

    print("Pid process one criado: ",codOne.pid)
    
    codTwo.start()
    print("Pid process two criado: ",codTwo.pid)
    
    # Espera a execução acabar (corrigido para .join() minúsculo)
    
    codOne.join() # espera terminar o processo um primeiro 
    
    codTwo.join() # espera terminar o processo dois
    
    endTime = time.time()  
    
    total_time = endTime - start_time

    print(f"Total de tempo que levamos para realizar o calculo: {total_time:.2f} segundos")
    
# Resumo:
# Criamos um código que realiza cria dóis processo para realizar de forma idependente
# o mesmo serviço... 