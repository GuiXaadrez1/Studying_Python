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

def salvar_tempo_sequencial(tempo):
    with open('tempo_sequencial.txt', 'w') as f:
        f.write(str(tempo))

def carregar_tempo_sequencial():
    try:
        with open('tempo_sequencial.txt', 'r') as f:
            return float(f.read())
    except FileNotFoundError:
        return None

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

        salvar_contagem(contagem_total, 'contagem_palavras.txt')

        mais_comuns = contagem_total.most_common(10)
        print("Top 10 palavras mais comuns:")
        for palavra, total in mais_comuns:
            print(f'{palavra}: {total}')

        print(f"\nTempo total: {tempo_total:.4f} segundos")

        if size == 1:
            # Salvar tempo sequencial como referência
            salvar_tempo_sequencial(tempo_total)
            print("Tempo sequencial salvo para comparação futura.")
        else:
            # Carregar tempo sequencial para comparação
            tempo_sequencial = carregar_tempo_sequencial()
            if tempo_sequencial is not None:
                speedup = tempo_sequencial / tempo_total
                eficiencia = speedup / size
                print(f"Speedup: {speedup:.4f}")
                print(f"Eficiência: {eficiencia:.4f}")
            else:
                print("Tempo sequencial não encontrado. Execute com apenas 1 processo para calcular.")
