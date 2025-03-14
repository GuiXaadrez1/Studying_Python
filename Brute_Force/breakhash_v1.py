import hashlib
import random
import time

# Função para gerar o hash MD5 de um texto
def gerar_md5(texto):
    md5 = hashlib.md5()
    md5.update(texto.encode('utf-8'))
    return md5.hexdigest()

#texto = "primeirofacil"
#hash_md5 = gerar_md5(texto)
#print(f'O hash MD5 do texto é: {hash_md5}')


# Função para tentar quebrar o hash
def break_hash(hash_original):
    list_string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = ''.join(list_string)
    lista = list(string)  
    random.shuffle(lista)  
    resultado = ''.join(lista)
    resultado = resultado[:10] 
    hash_gerado = gerar_md5(resultado)    
    return hash_gerado 


hash = "16c4f8b1d3e9bdb752f82b80a834fc9e"

# Loop de tentativa até encontrar o hash correto
while True:
    time_i = time.time() 
    
    hash_break = break_hash(hash)  
    
    time_f = time.time()  
    real_time = time_f - time_i  # Calcula o tempo gasto

    if hash_break == hash:
        print(f"Achou a hash:{hash_break}")
        print(f"Você demorou {real_time:.4f} segundos")  # Exibe o tempo de execução
        
        break  # Interrompe o loop após encontrar a correspondência
