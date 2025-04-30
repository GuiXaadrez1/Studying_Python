from mpi4py import MPI
import os
import sys
import time
from collections import Counter
import re

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        text = re.sub(r'[^a-zà-ÿ0-9\s]', '', text)  # remove pontuação, preserva acentos
        words = text.split()
    return words

def contar_palavras(palavras):
    return Counter(palavras)

def salvar_contagem(contagem, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        for palavra, total in contagem.items():
            f.write(f'{palavra} {total}\n')

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    inicio = time.time()

    if rank == 0:
        caminho_arquivo = os.path.join(os.getcwd(),'..','Historia.txt')
        palavras = read_txt(caminho_arquivo)

        # dividir lista de palavras entre os processos
        chunk_size = len(palavras) // size
        chunks = [palavras[i*chunk_size : (i+1)*chunk_size] for i in range(size)]

        # última parte pega o restante (para lidar com sobra)
        chunks[-1].extend(palavras[size*chunk_size:])
    else:
        chunks = None

    # Distribuir as partes para os processos
    palavras_local = comm.scatter(chunks, root=0)

    # Cada processo conta suas palavras
    contagem_local = contar_palavras(palavras_local)

    # Reunir todas as contagens no processo 0
    contagens_reunidas = comm.gather(contagem_local, root=0)

    if rank == 0:
        # Combinar as contagens
        contagem_total = Counter()
        for c in contagens_reunidas:
            contagem_total.update(c)

        fim = time.time()
        tempo_total = fim - inicio

        # Salvar contagem em arquivo
        salvar_contagem(contagem_total, 'contagem_palavras.txt')

        # Mostrar as 10 palavras mais comuns
        mais_comuns = contagem_total.most_common(10)
        print("Top 10 palavras mais comuns:")
        for palavra, total in mais_comuns:
            print(f'{palavra}: {total}')

        print(f"\nTempo total: {tempo_total:.4f} segundos")
