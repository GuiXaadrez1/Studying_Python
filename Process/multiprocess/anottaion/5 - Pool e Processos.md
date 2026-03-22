# Introdução

Se até agora você estava “criando processos”, agora você vai aprender a gerenciar paralelismo de forma eficiente, que é exatamente o que diferencia código acadêmico de código de produção.

## Pool de Processos (multiprocessing.Pool)

### O problema que o Pool resolve

Até agora você fazia isso:

```python

for i in range(100):
    Process(target=...)

```

Problemas graves:

- ❌ cria processos demais
- ❌ overhead absurdo
- ❌ pode travar o sistema
- ❌ não controla concorrência

### Definição formal

```python
    multiprocessing.Pool
```

Um gerenciador de processos que mantém um conjunto fixo de workers reutilizáveis.

### Modelo mental (arquitetura real) 

```bash
Main Process
     │
     ▼
   Task Queue
     │
 ┌───┼───────────┐
 ▼   ▼           ▼
W1  W2          WN   (workers)
```

- 👉 Você envia tarefas
- 👉 O Pool distribui automaticamente

## Criando um Pool

```python
from multiprocessing import Pool

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        pass
```

Explicação:

- processes=4 → número de workers

- with → garante fechamento correto

## Método mais importante: map

### Equivalente sequencial

```python
resultado:list = list(map(function,dados)) 
```

### Versão paralela

```python

from multiprocessing import Pool

def quadrado(x):

    return x * x

if __name__ == "__main__":

    with Pool(4) as pool:
    
        resultado = pool.map(quadrado, [1, 2, 3, 4])

    print(resultado)
```

### O que acontece internamente

- [1,2,3,4] → distribuído → workers → resultados → agregados

### Garantia importante:

- ✔ mantém ordem dos resultados
- ✔ bloqueante (espera tudo terminar)

## starmap (múltiplos argumentos)

### Problema

```python

def soma(a, b):
    return a + b

```

### Solução

```python

dados = [(1, 2), (3, 4), (5, 6)]

with Pool(4) as pool:

    resultado = pool.starmap(soma, dados)
```

### Internamente

- (1,2) → soma(1,2)
- (3,4) → soma(3,4)

## Execução assíncrona

Agora começa o nível mais interessante.

```python
from multiprocessing import Pool

def tarefa(x):
    
    return x * 2

if __name__ == "__main__":

    with Pool(2) as pool:
        
        resultado = pool.apply_async(tarefa, (10,))
        
        print("Executando em paralelo...")
        
        print(resultado.get())  # bloqueia aqui
```

## Objeto AsyncResult

```python
    resultado = pool.apply_async(...)
```

Você ganha:

```python
    resultado.get()        # pega resultado
    resultado.ready()      # terminou?
    resultado.successful() # deu certo?
```

### Uso profissional

Permite:

- ✔ pipeline assíncrono
- ✔ paralelismo sem bloqueio imediato

## imap (streaming de resultados)

### Diferença do map

| Método | Comportamento            |
| ------ | ------------------------ |
| map    | espera tudo              |
| imap   | retorna conforme termina |

### Exemplo

```python

from multiprocessing import Pool
import time

def tarefa(x):
    time.sleep(1)
    return x * 2

if __name__ == "__main__":

    with Pool(2) as pool:

        for resultado in pool.imap(tarefa, range(5)):
            print(resultado)
```

### Vantagem crítica

- ✔ menor uso de memória
- ✔ começa a processar antes de terminar tudo

## imap_unordered (máximo desempenho)

### Diferença
- imap           → mantém ordem
- imap_unordered → NÃO mantém ordem

### Exemplo

```python
for resultado in pool.imap_unordered(tarefa, range(5)):
    print(resultado)
```

### Quando usar?

- ✔ processamento pesado
- ✔ ordem não importa
- 👉 MELHOR PERFORMANCE

## Chunking (otimização crítica)

### Problema oculto

- Cada item enviado = overhead

### Solução: chunksize (processamento por blocos de memoria)

```python
pool.map(func, dados, chunksize=10)
```

### O que acontece

```bash
[1,2,3,4,5,6,7,8]

→ chunk 1: [1,2,3,4]
→ chunk 2: [5,6,7,8]
```

## Regra prática

| Cenário          | chunksize |
| ---------------- | --------- |
| tarefas pequenas | grande    |
| tarefas pesadas  | pequeno   |

## Número ideal de processos

### Regra base

```python
import os

os.cpu_count()
```

### Heurística

| Tipo      | Estratégia |
| --------- | ---------- |
| CPU-bound | = núcleos  |
| I/O-bound | > núcleos  |

### Exemplo

```pytohn
    Pool(os.cpu_count())
```

## Fechamento correto do Pool

### Forma manual

```python
    pool.close()
    pool.join()
```

### Forma profissional

```python
with Pool() as pool:
    ...
```

- ✔ evita vazamento de processo

## Erros comuns (nível real)

### Função não serializável

```python
def main():
    def interna(): pass  # ❌

pool.map(interna, dados)
``` 

### Esquecer __main__

- 💣 Windows quebra tudo

### Dados grandes demais

- ❌ gargalo em serialização

## Comparação final

| Abordagem | Uso                  |
| --------- | -------------------- |
| Process   | controle manual      |
| Pool      | produção / escala    |
| Queue     | comunicação          |
| Manager   | estado compartilhado |


## Insight avançado (nível engenharia)

O Pool implementa internamente:

```bash
→ Task Queue
→ Worker Loop
→ Load Balancer
→ Result Collector
```

👉 Ou seja:

- Você está usando um mini scheduler paralelo

