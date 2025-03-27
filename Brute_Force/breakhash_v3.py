import hashlib
import itertools
import string
import time
import multiprocessing

# Definição da hash alvo (troque conforme necessário)
hash_alvo = "b7a07aa24b0dd05a78653fe34443572d"

# Conjunto de caracteres permitidos (somente letras minúsculas)
charset = string.ascii_lowercase

# Define o tamanho da senha (testa apenas senhas com exatamente 7 caracteres)
tamanho_max_senha = 7

# Número de processos paralelos (limita se for maior que o necessário)
num_processos = min(multiprocessing.cpu_count(), len(charset) ** tamanho_max_senha)

# Evento para sinalizar quando a senha for encontrada
encontrado = multiprocessing.Event()

def gerar_md5(texto):
    """Gera o hash MD5 da string fornecida."""
    return hashlib.md5(texto.encode('utf-8')).hexdigest()

def quebrar_hash(process_id, inicio, passo, tempo_inicio):
    """Função executada por cada processo para tentar quebrar o hash."""
    tentativa_contador = 0  
    tamanho = tamanho_max_senha  # Considera apenas senhas do tamanho máximo

    for tentativa in itertools.islice(itertools.product(charset, repeat=tamanho), inicio, None, passo):
        if encontrado.is_set():  # Se outro processo encontrou a senha, sai
            return  

        senha = ''.join(tentativa)
        tentativa_contador += 1
        
        # Exibir progresso a cada 1.000.000 de tentativas
        if tentativa_contador % 1_000_000 == 0:
            tempo_decorrido = time.time() - tempo_inicio
            print(f"[Processo {process_id}] {tentativa_contador:,} tentativas... Tempo: {tempo_decorrido:.2f}s")

        # Verifica se a senha gerada corresponde ao hash alvo
        if gerar_md5(senha) == hash_alvo:
            tempo_total = time.time() - tempo_inicio
            print(f"\n[SUCCESS] Senha encontrada: {senha}")
            print(f"Tempo total de execução: {tempo_total:.2f} segundos")
            encontrado.set()  # Sinaliza para os outros processos que a senha foi encontrada
            return

def distribuir_trabalho():
    """Distribui o trabalho entre os processos."""
    tempo_inicio = time.time()  # Marca o início da execução
    
    with multiprocessing.Pool(processes=num_processos) as pool:
        pool.starmap(quebrar_hash, [(i, i, num_processos, tempo_inicio) for i in range(num_processos)])

if __name__ == "__main__":
    distribuir_trabalho()
    print("Finalizado!")
