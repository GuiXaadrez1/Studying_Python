# Introdução

Interfaces gráficas não respondem instantaneamente. Menus carregam, diálogos aparecem, processos executam em background. Agora vamos como construir automações mais robustas com menor risco de falha após algum componente falhar!

## O Problema da Sincronização

Considere este código:

```python
app = Application(backend="uia").start("notepad.exe")

window = app.window(title="Untitled - Notepad")

window.Edit.type_keys("teste")
```

Esta automação pode falhar, porque: 

```bash
Python executa instantaneamente
↓
Interface ainda não carregou
↓
Elemento não existe
↓
Erro
```

** Por isso usamos esperas controladas!**

## Método .wait()

O método .wait() espera um estado da interface.

Sintaxe:

```python
window.wait(condicao)
```

Estados possíveis: 

| Estado  | Significado           |
| ------- | --------------------- |
| exists  | elemento existe       |
| visible | está visível          |
| enabled | está habilitado       |
| ready   | pronto para interação |


Exemplos:

```python

# Bloqueia o código até que a interface/janela apareça
window.wait("visible")

# Esperando mútiplos estados
window.wait("ready")

# internamente isso significa: exists AND visible AND enebled

```

# Wait em Controles (Wappers)

Também podemos esperar controles wappers em específico, exemplo:

```python
edit = window.child_window(control_type="Edit")

edit.wait("visible")
```

Issso garante que o campo esteja disponível!

## Timeouts

Todos os waits possuem tempo limite.

```python
# espera a janela ficar visivel em até 10 segundos...
# Se nao aparecer acarreta em error!
window.wait("visible", timeout=10)
```

## Wait Existente no Pywinauto

Existe um método extremamente útil no PyWinAuto, chamado de wait_until_passes. Ele executa uma função até que funcione.

Exemplo:

```python

from pywinauto.timings import wait_until_passes

wait_until_passes(
    10,
    1,
    lambda: window.child_window(control_type="Edit").exists()
)
```

Parâmetros:

| parâmetro | significado  |
| --------- | ------------ |
| 10        | tempo máximo |
| 1         | intervalo    |
| função    | operação     |

## Retry Pattern

Automação profissional usa tentativas repetidas. Exemplo clássico:

```python
for _ in range(5):
    try:
        button.click()
        break
    except:
        time.sleep(1)
```

Esse padrão evita falhas quando: interface ainda não respondeu...

## Automação de Teclado

Muitas interfaces respondem melhor a atalhos de teclado.

Importação:

```python

    # importando o KeyBord
    from pywinauto.keyboard import send_keys

    # Digitando a lerea "a"
    send_keys("a")

```

Atalhos: 

| símbolo | tecla |
| ------- | ----- |
| ^       | CTRL  |
| %       | ALT   |
| +       | SHIFT |

Exemplos

Salvar:

```python
    send_keys("^s")
```

Copiar:

```python
    send_keys("^c")
```

Selecionar tudo:

```python
send_keys("^a")
```

## Digitação Avançada

Método:

```python
    type_keys()
```

Parâmetros importantes:

| parâmetro     | função             |
| ------------- | ------------------ |
| with_spaces   | permite espaço     |
| pause         | pausa entre teclas |
| with_newlines | permite ENTER      |

Exemplo:

```python
    edit.type_keys("Automacao", with_spaces=True)
```

### digitação realista

```python
    edit.type_keys("teste", pause=0.05)
```

isso simula um usuário real

## Automação de Mouse

Importação: 

```python
from pywinauto.mouse import click
```

Exemplos de uso e métodos:

```python

# click de mouse
from pywinauto.mouse import click
from pywinauto.mouse import double_click

# Drag and Drop

from pywinauto.mouse import press, release

# clicando em coordeandas 
click(coords=(500,300))

double_click(coords=(400,200))

press(coords=(300,300))
release(coords=(500,500))

```

## Esperando Controles Dinâmicos

Muitas interfaces criam controles dinamicamente 

Exemplo:

```bash
clicar botão
↓
janela popup aparece
```

Código correto:

```python
button.click()

popup = app.window(title="Confirm")

popup.wait("visible")
```

## Sincronização com wait_cpu_usage_lower

Método extremamente útil.

```python
app.wait_cpu_usage_lower()
```

Ele espera o processo terminar tarefas internas...

Exmeplo: 

```python
app.wait_cpu_usage_lower(threshold=5)
```

útil em sistemas pesados!

## Estratégias Anti-Falha

Regra 1 — Sempre usar wait

```python

# Errado:
button.click()

# Certo:
button.wait("enabled")
button.click()
```

Regra 2 — Nunca confiar em tempo fixo

```python

# Errado: 

time.sleep(3)

# Certo:

wait()

```

Regra 3 — Validar resultado (controle de interface) - Retry Pattern

```python

if popup.exists():
    popup.OK.click()

```

## Exemplo de Script Completo e Robusto!

```python
from pywinauto import Application
from pywinauto.keyboard import send_keys

app = Application(backend="uia").start("notepad.exe")

window = app.window(title="Untitled - Notepad")

window.wait("ready")

edit = window.child_window(control_type="Edit")

edit.wait("visible")

edit.type_keys("Automacao robusta", with_spaces=True)

send_keys("^s")

save = app.window(title="Save As")

save.wait("visible")

filename = save.child_window(control_type="Edit")

filename.type_keys("arquivo.txt")

save.child_window(title="Save", control_type="Button").click()
```
