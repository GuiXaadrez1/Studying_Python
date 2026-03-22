## O que é a biblioteca multiprocessing?

A multiprocessing é uma biblioteca nativa do Python que fornece:

- Uma abstração de alto nível para criação, controle e comunicação entre processos


Ela funciona como uma camada sobre:

- chamadas de sistema (fork, spawn)
- IPC (Inter Process Communication)
- Gerenciamento de processos do SO

## Módulos internos (visão estrutural)

A biblioteca não é apenas Process. Ela é composta por vários blocos:

```bash
multiprocessing/
├── Process # criacao de processos independentes
├── Pool
├── Queue # filas 
├── Pipe # canal de comunicao entre processos
├── Manager # Mensageiros
├── Value / Array
├── shared_memory # compartilhamento de memória
├── synchronization (Lock, Event, Semaphore)
```

- Pense nela como um mini sistema operacional de paralelismo dentro do Python.

## Modelo de uso (nível macro)

Todo uso da biblioteca segue esse padrão:

```bash
1. Definir tarefa
2. Criar processos
3. Enviar dados
4. Executar
5. Sincronizar
6. Coletar resultado
```

