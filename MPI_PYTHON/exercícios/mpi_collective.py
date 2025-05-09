# Usando Scattering
'''
Distribui diferentes pedaços de uma lista (neste caso, dicionários personalizados)
para vários processos paralelos. O processo de rank 0 cria os dados e usa scatter
para enviar um pedaço para cada processo.

'''

if __name__ == "__main__":

    from mpi4py import MPI

    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    worker = comm.Get_rank()

    # Se o processo for o de rank 0
    if worker == 0:
        # Cria uma lista de dicionários personalizados
        data = [{"Dados no rank " + str(i): i} for i in range(0, size)]
    else: 
        data = None

    # O processo de rank 0 distribui os dados entre todos usando scatter
    data = comm.scatter(data, root=0)

    # Cada processo exibe o dado que recebeu
    print(worker, data)

'''
O que é comunicação coletiva no MPI?

    Comunicação coletiva é quando todos os processos de um grupo participam
    simultaneamente de uma operação de comunicação. Ou seja, não é apenas um
    processo enviando ou recebendo individualmente (como na comunicação ponto a ponto),
    mas todos os processos estão envolvidos em uma ação conjunta.

Características da comunicação coletiva:

    - Todos os processos chamam a mesma função (como broadcast, scatter, gather, etc.).
    - A comunicação é coordenada pelo sistema MPI, o que tende a ser mais eficiente.
    - É usada para dividir, reunir ou sincronizar dados entre todos os processos.

+-------------+--------------------------------------------------------------+
| Função MPI  | O que faz                                                    |
+-------------+--------------------------------------------------------------+
| broadcast   | Um processo envia a mesma informação para todos os outros.  |
| scatter     | Um processo distribui diferentes pedaços de dados.          |
| gather      | Todos os processos enviam dados para um processo central.   |
| allgather   | Cada processo envia dados e todos recebem tudo.             |
| reduce      | Dados são combinados (ex: soma, máximo, média, etc.).       |
| barrier     | Sincroniza todos os processos (espera todos chegarem).      |
+-------------+--------------------------------------------------------------+
'''
