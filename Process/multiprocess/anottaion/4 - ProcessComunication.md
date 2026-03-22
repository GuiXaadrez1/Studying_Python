## Comunicação entre Processos (IPC — Inter Process Communication)

### O problema fundamental

Você já entendeu:

- ✔ processos são isolados
- ✔ não compartilham memória

Então surge o problema central:

- Como processos trocam dados de forma segura e eficiente?

### Estratégias de IPC no multiprocessing

A biblioteca oferece 4 abordagens principais:

1. Queue        → Alta abstração (mais usada)
2. Pipe         → Comunicação direta (baixo nível)
3. Manager      → Estruturas compartilhadas
4. SharedMemory → Alto desempenho (baixo nível)

## Queue (fila de mensagens)

### Definição

```python   
multiprocessing.Queue
```

Uma fila segura entre processos baseada em FIFO (First In, First Out)

### Arquitetura interna

```bash
Processo A → (PUT) → [ BUFFER IPC ] → (GET) → Processo B
```

- ✔ Usa pipes + locks internamente
- ✔ Thread-safe e process-safe

### Exemplo base

```python

from multiprocessing import Process, Queue

def produtor(q):
    
    for i in range(5):
        
        print(f"Produzindo {i}")
        
        q.put(i)

def consumidor(q):
    
    while not q.empty():
        
        valor = q.get()
        
        print(f"Consumindo {valor}")

if __name__ == "__main__":
    
    q = Queue()

    p1 = Process(target=produtor, args=(q,))
    p2 = Process(target=consumidor, args=(q,))

    p1.start()
    p1.join()  # garante produção antes

    p2.start()
    p2.join()
```

### Problema clássico (armadilha)

```python
while not q.empty():
```

- ❌ NÃO é confiável em concorrência real

- 👉 Porque outro processo pode alterar a fila simultaneamente

### Solução correta (padrão profissional)

- Use sentinela (poison pill):

```python

def produtor(q):
    for i in range(5):
        q.put(i)
    q.put(None)  # sinal de fim

def consumidor(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumindo {item}")
```

## Insight de engenharia

👉 Queue transforma seu sistema em:

- Sistema baseado em mensagens (Message Passing)

Isso é o mesmo modelo usado em:

- Kafka
- RabbitMQ
- sistemas distribuídos reais

## Pipe (comunicação ponto a ponto)

### Definição

```pytohn
multiprocessing.Pipe()
```

Retorna:

```python
conn1, conn2
```

### Modelo mental

```bash
Processo A ⇄ Processo B
```

👉 Comunicação direta (sem fila)

### Exemplo

```python

from multiprocessing import Process, Pipe

def filho(conn):
    
    conn.send("Mensagem do filho")
    conn.close()

if __name__ == "__main__":
    
    pai_conn, filho_conn = Pipe()

    p = Process(target=filho, args=(filho_conn,))
    p.start()

    print(pai_conn.recv())

    p.join()
```

### Quando usar Pipe?

- ✔ comunicação simples
- ✔ baixa latência
- ✔ 1 para 1
- ❌ não escala bem
- ❌ sem buffering avançado

## Manager (estado compartilhado)

### Definição

```python
multiprocessing.Manager()
```

- Cria um servidor intermediário que mantém objetos compartilhados

### Estruturas suportadas

- manager.list()
- manager.dict()
- manager.Value()

### Exemplo

```python

from multiprocessing import Process, Manager

def worker(lista):
    lista.append("processo")

if __name__ == "__main__":
    
    with Manager() as manager:
        
        lista = manager.list()

        processos = []
        
        for _ in range(3):
           
            p = Process(target=worker, args=(lista,))
            p.start()
            processos.append(p)

        for p in processos:
            
            p.join()

        print(lista)
```

## Arquitetura real

- Processos → Proxy → Servidor Manager → Estado real

### Problema crítico

- ❗ Manager é lento

Porque:

- usa proxy
- usa serialização
- usa IPC interno

- 👉 NÃO use para alto desempenho

## Comparação técnica

| Técnica       | Performance | Escalabilidade | Complexidade |
| ------------- | ----------- | -------------- | ------------ |
| Queue         | Média       | Alta           | Baixa        |
| Pipe          | Alta        | Baixa          | Média        |
| Manager       | Baixa       | Média          | Baixa        |
| Shared Memory | Muito alta  | Alta           | Alta         |

## Padrões de arquitetura com Queue

### Produtor/Consumidor

```bash
Produtores → Queue → Consumidores
```

### Fan-out

```bash
        → Worker 1
Queue → → Worker 2
        → Worker 3
```

### Pipeline

```bash
Etapa 1 → Etapa 2 → Etapa 3
   Q1        Q2
```

## Deadlocks e problemas reais

### Deadlock clássico

```python
q.put(muito_dado)
# ninguém consumindo
```

👉 fila enche → trava

### Bloqueio em get()

```python
q.get()
```

👉 bloqueia indefinidamente

### Solução

```python
q.get(timeout=5)
```

ou:

```python
q.get_nowait()
```

## Serialização (o ponto crítico)

Tudo que passa entre processos:

- → é serializado (pickle)
- → enviado
- → desserializado

## Implicações

- ✔ objetos grandes → lento
- ✔ objetos complexos → erro

## Exemplo problemático

```python
q.put(lambda x: x)  # ERRO
```

## Boas práticas

- ✔ usar tipos simples
- ✔ evitar objetos pesados
- ✔ chunk de dados

## Insight avançado (nível arquitetura)

Quando você usa multiprocessing, você está implicitamente adotando:

- Modelo Actor / Message Passing

Cada processo:

- recebe mensagens
- processa
- responde

👉 Isso é exatamente como sistemas distribuídos funcionam