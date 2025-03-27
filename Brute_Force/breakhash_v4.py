import hashlib
import time
import itertools
import multiprocessing

# Função para gerar o hash MD5 de um texto
def gerar_md5(texto):
    md5 = hashlib.md5()
    md5.update(texto.encode('utf-8'))
    return md5.hexdigest()

# Função que tenta quebrar o hash em um intervalo de combinações
def break_hash_intervalo(start, end, list_string, hash_procurado, resultado_queue, progresso_queue, processo_id):
    tentativa_count = 0
    time_i = time.time()  # Marca o tempo inicial para as tentativas
    for comb in itertools.product(list_string, repeat=10):
        resultado = ''.join(comb)
        hash_gerado = gerar_md5(resultado)

        tentativa_count += 1

        # Enviar o progresso a cada 1.000.000 tentativas, incluindo o ID do processo
        if tentativa_count % 1000000 == 0:
            time_f = time.time()  # Marca o tempo final
            real_time = time_f - time_i  # Calcula o tempo gasto
            progresso_queue.put((tentativa_count, real_time, processo_id))  # Envia o progresso, tempo e id do processo para a fila

        if hash_gerado == hash_procurado:
            resultado_queue.put((hash_gerado, resultado, processo_id))  # Envia o resultado e o id do processo para a fila
            return  # Termina a função assim que encontrar o hash

    resultado_queue.put(None)  # Coloca um None para indicar que a tarefa foi concluída sem sucesso

# Função para dividir o trabalho entre os processos
def break_hash_multiprocessado(hash_procurado):
    list_string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num_processos = 2 # Número de processos
    combinacoes_total = 26 ** 10  # Total de combinações de 10 caracteres
    tamanho_intervalo = combinacoes_total // num_processos  # Tamanho do intervalo para cada processo

    # Fila para coletar os resultados dos processos
    resultado_queue = multiprocessing.Queue()
    progresso_queue = multiprocessing.Queue()

    processos = []
    for i in range(num_processos):
        start = i * tamanho_intervalo
        end = (i + 1) * tamanho_intervalo
        if i == num_processos - 1:
            end = combinacoes_total  # O último processo vai até o fim
        p = multiprocessing.Process(target=break_hash_intervalo, args=(start, end, list_string, hash_procurado, resultado_queue, progresso_queue, i))
        processos.append(p)
        p.start()

    # Monitorando o progresso
    tentativas_feitas = 0
    while any(p.is_alive() for p in processos):
        if not progresso_queue.empty():
            tentativas_feitas, tempo, processo_id = progresso_queue.get()
            print(f"Processo {processo_id}: Tentativas até agora: {tentativas_feitas}, Tempo gasto até agora: {tempo:.4f} segundos")

    # Aguardar os processos terminarem
    for p in processos:
        p.join()

    # Verificar se algum processo encontrou a hash
    while not resultado_queue.empty():
        resultado = resultado_queue.get()
        if resultado is not None:
            return resultado  # Retorna o hash, o texto e o processo que encontrou
    return None  # Caso nenhum processo tenha encontrado

# Função principal para rodar o processo e gerar o relatório
def main():
    hash_procurado = "16c4f8b1d3e9bdb752f82b80a834fc9e"

    # Medindo o tempo de execução real
    time_i = time.time()

    resultado = break_hash_multiprocessado(hash_procurado)

    time_f = time.time()  # Marca o tempo final
    real_time = time_f - time_i  # Calcula o tempo gasto

    if resultado:
        hash_gerado, texto, processo_id = resultado
        print(f"Processo {processo_id} encontrou a hash '{hash_gerado}' para a string '{texto}'!")
    else:
        print("Não encontrou a hash.")

    print(f"Tempo total de execução: {real_time:.4f} segundos")

if __name__ == "__main__":
    main()
