# Classe Process (núcleo da biblioteca)

## Definição forma desta Classe...

uma unidade independente de execução gerenciada pelo sistema operacional

```python

import sys
# importacao da Classe no Módulo...
from multiprocessing import Process

def somar_two_numbers(*args):
    """
    Soma os números passados, limitando a entrada a no máximo dois argumentos.

    O asterisco (*) antes do parâmetro 'args' indica o empacotamento de argumentos 
    posicionais (Variadic Arguments). Isso significa que todos os valores passados 
    na chamada da função serão reunidos em uma tupla única chamada 'args'.

    Regras de execução:
    1. O programa verifica o comprimento (len) da tupla 'args'.
    2. Se houver mais de 2 elementos, exibe uma mensagem de erro e encerra 
       a execução do script via sys.exit(0).
    3. Caso contrário, utiliza a função sum() para somar os elementos da tupla.

    Args:
        *args: Argumentos numéricos variáveis que serão empacotados em uma tupla.

    Returns:
        int/float: A soma total dos elementos contidos em args.
    """
    if len(args) > 2:
        print("Erro: Apenas dois números são permitidos.")
        sys.exit(0)

    return sum(args)

# Assinatura completa da class

Process(
    group=None,
    target=None, # assinatura da funcao que sera executada por esse processo!
    name=None, # Apenas identificação (debug/log)
    args=(), # Argumentos posicionais -> sempre em tuplas!
    kwargs={}, # Argumentos nomeados -> possivel acessâ-los por indícies 
    daemon=None # Define se o processo é dependente do processo pai! ✔ morre quando o processo principal morre ❌ não pode criar filhos
)

codOne:Process = Process(target=somar_two_numbers) 

```

## Ciclo de vida do processo

```bash
NEW → STARTED → RUNNING → TERMINATED
```

## Principais métodos:

```python

# Cria o processo no sistema operacional 
codeOne.start()

# Executa diretamente (sem criar novo processo)
codeOne.run()

# Bloqueia até terminar a execucao do processo e ir para a próximo instrução
codeOne.join()

# mata o processo (criado) forçadamente
codeOne.terminate()

# verifica o estado do processo(ciclo de vida)
is_alive()
```

## Exemplo completo (nível engenharia)

```python

from multiprocessing import Process
import os
import time

def worker(nome):
    
    print(f"[{nome}] PID: {os.getpid()}")
    
    time.sleep(2)
    
    print(f"[{nome}] Finalizado")

if __name__ == "__main__":
    processos = []

    for i in range(3):
        p = Process(target=worker, args=(f"P{i}",))
        processos.append(p)

    # START
    for p in processos:
        p.start()

    # MONITORAMENTO
    for p in processos:
        print(f"Processo {p.pid} ativo? {p.is_alive()}")

    # JOIN
    for p in processos:
        p.join()

    print("Todos finalizaram")

```