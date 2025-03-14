import hashlib
import time
import itertools

# Função para gerar o hash MD5 de um texto
def gerar_md5(texto):
    md5 = hashlib.md5()
    md5.update(texto.encode('utf-8'))
    return md5.hexdigest()

# Função para tentar quebrar o hash
def break_hash_sequencial():
    list_string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # Gerando todas as combinações possíveis de 6 caracteres
    for comb in itertools.product(list_string, repeat=10):
        resultado = ''.join(comb)
        hash_gerado = gerar_md5(resultado)
        yield hash_gerado, resultado  # Retorna o hash gerado e a string gerada

hash = "16c4f8b1d3e9bdb752f82b80a834fc9e"

# Medindo o tempo de execução real
time_i = time.time()  # Marca o tempo inicial

a = 0
for hash_break, texto in break_hash_sequencial():
    a += 1
    if a % 1000000 == 0:
        print(texto)

    if hash_break == hash:
        time_f = time.time()  # Marca o tempo final
        real_time = time_f - time_i  # Calcula o tempo gasto
        print(f"Achou a hash '{hash_break}' para a string '{texto}'!")
        print(f"Você demorou {real_time:.4f} segundos")
        break  # Interrompe o loop após encontrar a correspondência
