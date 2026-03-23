# Biblioteca subprocess é na verdade uma ponte entre o programa python e o sistema operacional!

# 👉 O subprocess resolve isso oferecendo controle total sobre processos filhos (child processes).

# Quando você usa subprocess, você está:
# - Criando um processo filho que roda fora do seu programa Python
# - Arquitetura simplificada:

'''
[Seu Python]
     │
     ▼
[subprocess]
     │
     ▼
[Processo do SO (cmd, exe, script, etc)]
'''

if __name__ == "__main__":

    import os 
    import sys 
    import subprocess

    # executa um comando e espera terminar... 
    # shell=True permite usar comandos internos como 'dir'
    # capture_output=True faz o Python guardar o resultado em vez de só jogar na tela
    # text=True transforma os bytes de saída em texto legível
    # resultado = subprocess.run(['dir'], shell=True, capture_output=True, text=True)
    
    subprocess.run(['dir'], shell=True, cwd='C:\\')
    
    # print(resultado.stdout)