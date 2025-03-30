import numpy as np
import pandas as pd
from multiprocessing import Pool
import os
import time

# Função para calcular uma linha de C
def calc_row(i, A, B):
    return np.dot(A[i], B)

# Função para multiplicar as matrizes em paralelo
def parallel_matrix_multiply(A, B, num_processes):
    pool = Pool(processes=num_processes)
    results = pool.starmap(calc_row, [(i, A, B) for i in range(A.shape[0])])
    pool.close()
    pool.join()
    return np.array(results)

# Função para multiplicar as matrizes de forma serial (1 processador)
def serial_matrix_multiply(A, B):
    return np.dot(A, B)

# Proteção para Windows
if __name__ == '__main__':
    # Verificar diretório atual
    print("Diretório atual:", os.getcwd())

    # Caminho da Matrix A
    A_path = os.path.join(os.getcwd(),'data','matrix_A_1000.csv')

    # Caminho da Matrix B
    B_path = os.path.join(os.getcwd(),'data','matrix_B_1000.csv')

    # Carregar as matrizes de arquivos .csv
    A = pd.read_csv(A_path, header=None).values  # Matriz A
    B = pd.read_csv(B_path, header=None).values  # Matriz B

    # Multiplicação serial (1 processador)
    start_time = time.time()
    C_serial = serial_matrix_multiply(A, B)
    time_serial = time.time() - start_time
    print(f"Tempo de execução serial: {time_serial:.4f} segundos")

    # Salvar o resultado da multiplicação com 1 processador em um arquivo CSV
    result_path_serial = 'resultado_multiplicacao_serial.csv'
    pd.DataFrame(C_serial).to_csv(result_path_serial, index=False, header=False)
    print(f"Resultado da multiplicação com 1 processador salvo em '{result_path_serial}'")

    # Multiplicação com 1 até 20 processadores
    for num_processors in range(1, 21):  # De 1 a 20 processadores
        start_time = time.time()
        C_parallel = parallel_matrix_multiply(A, B, num_processors)
        time_parallel = time.time() - start_time
        print(f"Tempo de execução com {num_processors} processadores: {time_parallel:.4f} segundos")

        # Salvar o resultado da multiplicação em um arquivo CSV
        result_path_parallel = f'resultado_multiplicacao_{num_processors}_processadores.csv'
        pd.DataFrame(C_parallel).to_csv(result_path_parallel, index=False, header=False)
        print(f"Resultado da multiplicação com {num_processors} processadores salvo em '{result_path_parallel}'")
