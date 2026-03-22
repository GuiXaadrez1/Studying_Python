# Introdução

Agora você entrou na camada que realmente define se alguém entende paralelismo de verdade ou só usa API. Aqui começa o nível de engenharia de sistemas concorrentes:

- ⚠️ memória compartilhada + sincronização + controle de concorrência

## Memória Compartilhada e Sincronização

### O problema central

Até agora:

- ✔ processos isolados
- ✔ comunicação via mensagem

Mas isso tem custo:

- serialização (pickle)
- cópia de dados
- latência

## 💡 Nova necessidade

- Compartilhar dados diretamente na memória (sem cópia)

### Memória Compartilhada (Shared Memory)

## Definição

Memória acessível por múltiplos processos simultaneamente.

- 👉 Sem serialização
- 👉 Sem cópia

### Ferramentas disponíveis

```bash
multiprocessing.Value
multiprocessing.Array
multiprocessing.shared_memory
```

### Value (valor compartilhado simples)


```python

from multiprocessing import Process, Value

def incrementa(contador):
    contador.value += 1

if __name__ == "__main__":

    contador = Value('i', 0)  # inteiro

    processos = []

    for _ in range(5):
        
        p = Process(target=incrementa, args=(contador,))
        
        p.start()
        
        processos.append(p)

    for p in processos:
        
        p.join()

    print(contador.value)
```

### Problema GRAVE (race condition)

Esse código pode imprimir:

```bash
2, 3, 4... (valor incorreto)
```

## Race Condition (condição de corrida)

### Definição formal

Quando múltiplos processos acessam/modificam o mesmo dado simultaneamente, causando inconsistência.

### O que acontece internamente

```bash
Processo A lê valor = 0
Processo B lê valor = 0

Processo A escreve 1
Processo B escreve 1  ← sobrescreve
```

💣 Resultado:

- Perda de dados


## Estratégias para combanter o race condition

### Lock (trava de exclusão mútua)

```python
multiprocessing.Lock
```

Garante que apenas UM processo acesso o recurso por vez.

### Correção do exemplo anterior

```python
from multiprocessing import Process, Value, Lock

def incrementa(contador, lock):
    with lock:
        contador.value += 1

if __name__ == "__main__":
    contador = Value('i', 0)
    lock = Lock()

    processos = []
    for _ in range(5):
        p = Process(target=incrementa, args=(contador, lock))
        p.start()
        processos.append(p)

    for p in processos:
        p.join()

    print(contador.value) # resultado correto == 5
```

### Custo oculto

Locks introduzem:

- ❌ contenção
- ❌ perda de paralelismo

- 👉 trade-off clássico
