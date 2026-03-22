## Conceito de isolamento de memórias Continuacao cap 2

Como cada processo com multiprocessing são independente... Isto é nao dependem um dos outros para realizar determinada execucao... Vamos olhar o exemplo abaixo:

```python

# Criando um estado Global 
x = 10

def altera():
    
    # Devemos evitar esse tipo de procedimento na contrucao do código => Evitar estado global

    global x
    
    x = 99

if __name__ == "__main__":
    
    p = Process(target=altera)
    
    p.start()
    
    p.join()

    print(x)  # continua 10
```

👉 Isso NÃO é bug
👉 Isso é arquitetura de processos

```bash
Processo Pai
│
├── copia memória
│
└── Processo Filho (isolado)
```

## Implicação prática

Você NÃO pode:

- ❌ compartilhar variáveis diretamente
- ✔ deve usar mecanismos de IPC

## Multiprocessamento em lote (loop de processos)

Problema comum:

Executar várias tarefas paralelas:

```python

for i in range(10):
    Process(...)

```

Padrão profissional:

```python

from multiprocessing import Process

def tarefa(n):
    
    print(f"Processando {n}")

if __name__ == "__main__":
    
    processos = []

    for i in range(5):
        
        p = Process(target=tarefa, args=(i,))
        
        processos.append(p)
        
        p.start()

    for p in processos:
        
        p.join()
```

### Problema oculto do padrão profissional (importante) 

Isso pode causar:

excesso de processos
saturação de CPU
overhead alto

👉 Aqui nasce a necessidade do Pool (capítulo futuro)

### tabela dos problemas comuns

| Problema                       | Causa                 |
| ------------------------------ | --------------------- |
| Código executa múltiplas vezes | falta do `__main__`   |
| Variável não atualiza          | isolamento de memória |
| Travamento                     | deadlock              |
| Lentidão                       | overhead alto         |


## Boas práticas

### Proteção de entrada (CRÍTICO)

```python
    if __name__ == "__main__":
```

Sem isso:

💣 loop infinito de criação de processos (Windows)

### Funções devem ser serializáveis

```python 
def func():
    pass
```

❌ Não funciona muito bem bom lambda:

```python
lambda x: x
```

### Evitar estado global! 

### Evitar objetos complexos

Tudo é serializado:

- conexões DB ❌
- sockets ❌
- objetos GUI ❌

## Diagnóstico e Debug

### Identificando processos

```python
import os

print(os.getpid())
print(os.getppid())
```

### Logs estruturados

```python
print(f"[PID {os.getpid()}] executando...")
```