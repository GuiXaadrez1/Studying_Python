# Application Object to PyWinAuto

Agora vamos falar sobre a materilazao do objeto de Applicacao do PyWinAuto

```python

from pywinauto import Application

# 1 Iniciando o Objeto de Aplicacao - Essa classe representa o processo da aplicação.
# Ela representa um processo Windows sendo controlado pelo Python.
app:Application = Application()

# iniciando o Programa
app = Application().start("notepad.exe")

# Obs.: Aqui estamos abrindo um novo programa... Se esse programa já estiver aberto...
# vamos inicar outro programa com PyWinAuto

```

## Fluxo Interno

```Bash
start()
   ↓
CreateProcess
   ↓
Windows handle (Escuta eventos...)
   ↓
Application object
```

O método retorna um objeto Application já conectado ao processo.

## Iniciando com backend específico

O pywinauto possui dois motores de automação.

```bash
win32
uia
```

Exemplo:

```pytohn
   app = Application(backend="uia").start("notepad.exe")
```
## Diferença

| Backend | Tipo de aplicação |
| ------- | ----------------- |
| win32   | apps antigos      |
| uia     | apps modernos     |

Hoje UIA é o mais recomendado.

## Conectando a Programs Já Abertos!

Nem sempre queremos abrir o programa. Às vezes ele já está em execução. Para isso usamos .connect().

### Método .connect()

Sintaxe:

   - Application().connect(...)

Ele conecta ao processo existente.


### Conectando pelo nome da janela ( da árvore de componentes...)

```python
   app = Application().connect(title="Untitled - Notepad")
```

Conectando pelo processo ( neste caso o PID do proceso)

``` python
   app = Application().connect(process=1234)
```

## Conectando pelo caminho

```python
   app = Application().connect(path="notepad.exe")
```

## Métodos Essenciais da Classe Application

| Método      | Função             |
| ----------- | ------------------ |
| `start()`   | inicia programa    |
| `connect()` | conecta a programa |
| `window()`  | obtém janela       |
| `windows()` | lista janelas      |
| `kill()`    | encerra processo   |