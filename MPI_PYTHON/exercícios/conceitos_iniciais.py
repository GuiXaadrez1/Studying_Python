# vamos criar um grupo mpi associado a um comunicador ("MPI_COMM_WORLD")
# um tamanho de processo mpi por identificador (RANK)
# MPI_COMM_WORLD -> comunicador principal, inclui todos os processos que começaram a execução
# comm.Get_size() retorna a quantidade de processos que está neste comunicador
# comm.Get_Rank() retorna o id - identificador do processo atual naquela GRUPO

from mpi4py import MPI

comm = MPI.COMM_WORLD # grupo de processos, no comunicador central
worker = comm.Get_rank()# id - identificador  do processo também conhecido como trabalhadores (worker)
size = comm.Get_size()# método que retorna a quantidade de trabalhadores dentro do grupo, ou seja, o tamanho do grupo mpi

print(f"Hello world, esse e o tranalhador: {worker}, de {size} trabalhadores")