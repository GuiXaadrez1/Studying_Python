import random
import os

def gerar_arquivo_valores(nome_arquivo: str, tamanho_mb: int):
    valores_possiveis = [-1, 0, 1]
    tamanho_alvo_bytes = tamanho_mb * 1024 * 1024  # MB para bytes

    with open(nome_arquivo, 'w') as f:
        tamanho_atual = 0
        while tamanho_atual < tamanho_alvo_bytes:
            valor = random.choice(valores_possiveis)
            linha = f"{valor}\n"
            f.write(linha)
            tamanho_atual += len(linha.encode('utf-8'))  # medir tamanho real

    tamanho_final = os.path.getsize(nome_arquivo) / (1024 * 1024)
    print(f"Arquivo '{nome_arquivo}' gerado com {tamanho_final:.2f} MB.")

if __name__ == "__main__":
    gerar_arquivo_valores("valores_500mb.txt", 500)
