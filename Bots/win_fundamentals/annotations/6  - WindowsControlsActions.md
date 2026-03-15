# Introducao 

O que vimos até agora foi o básico de PyWinAuto, agora vamos nos aperfeiçoar...
antes controlavamos a aplicacao e a janela, agora vamos controlar da janela até uma ação

```bash
Window → Controls → Actions
```

Vamos manipular os elementos internos da interface (janela).

## WindowSpecification

Quando usamos:

```python
window = app.window(title="Untitled - Notepad")
```

O objeto retornado não é ainda a janela real. Ele é um objeto de especificação. Tipo interno: **WindowSpecification**

Esse objeto funciona como um seletor de interface. Ele guarda critérios de busca. Exemplo conceitual:

```bash
WindowSpecification
    title = "Untitled - Notepad"
```

Somente quando você executa uma ação o pywinauto resolve a busca. Exemplo:

```
window.print_control_identifiers()
```

Nesse momento ocorre:

```bash
WindowSpecification
      ↓
Search UI tree
      ↓
Resolve element
      ↓
Wrapper Object
```

## Descoberta de Controles

Toda automação depende de descobrir como os elementos da interface são estruturados.

Ferramentas para isso:

```bash
Inspect.exe
WinSpy
print_control_identifiers()
```

A mais usada dentro do Python é:

``` python
window.print_control_identifiers()
```

Exemplo completo: 

```python
from pywinauto import Application

app = Application(backend="uia").start("notepad.exe")

window = app.window(title="Untitled - Notepad")

# Retornar uma arvore de elementos da janela para identificacao de componentes/controles
window.print_control_identifiers()
```

Saída típica:

```bash
Window - 'Untitled - Notepad'

   | MenuBar
   |    | MenuItem - File
   |    | MenuItem - Edit
   |    | MenuItem - View

   | Edit
   | StatusBar
```

Isso significa que a estrutura é:

```bash
Window
   ├ MenuBar
   │   ├ File
   │   ├ Edit
   │   └ View
   ├ Edit
   └ StatusBar
```

Ou seja:

```bash
Edit = campo de texto
MenuBar = menu superior
StatusBar = barra inferior
```

##  Método child_window()

Este é o método mais importante de toda a biblioteca. Ele permite acessar qualquer controle da interface.

Sintaxe:

```bash
    window.child_window(...)
```

Parâmetros:

| parâmetro    | significado       |
| ------------ | ----------------- |
| title        | texto do controle |
| control_type | tipo de controle  |
| auto_id      | id interno        |
| class_name   | classe Windows    |


Exemplo: 


```python

# encontrando um componente na janela pelo control_type
edit = window.child_window(control_type="Edit")

# encontrando um componente na janela pelo control_type e title
button = window.child_window(title="OK", control_type="Button")

file_menu = window.child_window(title="File", control_type="MenuItem")
```

## Seletores Robustos
Automação frágil geralmente acontece quando usamos seletores ruins.

Exemplo Ruim: 

```python
window.child_window(title="OK")
```

Se o idioma mudar:

```bash
OK → Confirmar
```

O robô quebra.

Exemplo Bom ao usar o identificador interno: 

```python
window.child_window(auto_id="12345", control_type="Button")
```

Propriedade de seletores recomendadas:

```bash
1 auto_id
2 control_type
3 class_name
4 title
```

## Wrapper Objects

Quando um controle é encontrado, o pywinauto cria um wrapper object. Esse wrapper representa o controle.

Tipos comuns:

```bash
ButtonWrapper
EditWrapper
ComboBoxWrapper
ListViewWrapper
```

Exemplo:

```python
    edit = window.child_window(control_type="Edit").wrapper_object()
```

Agora edit possui métodos específicos.

## Métodos de Interação

Cada wrapper possui métodos específicos.

```python

# Interacao que simula o evendo de escrever...
edit.type_keys("Hello world", with_spaces=True)

# Interacao que obtem o texto na janela
edit.window_text()

# Interacao que limpa o texto na janela...
edit.set_edit_text("")

# iteracao que simula o evento de click
button.click()

button.click_input()

# Diferença entre click e click_input...

'''

| método      | funcionamento     |
| ----------- | ----------------- |
| click       | mensagem interna  |
| click_input | simula mouse real |

'''

```

## Navegação Hierárquica

Controles podem ter filhos. Exemplo:


```bash
Window
   MenuBar
      File
         Save
         Open
```

Para acessar diretamente: 

```python
    save = window.child_window(title="Save", control_type="MenuItem")
```

Ou navegando passo a passo: 

```python

menu = window.child_window(control_type="MenuBar")

file = menu.child_window(title="File")

save = file.child_window(title="Save")

```

## Exemplo Completo de Automação

Objetivo: 

```bash
abrir notepad
digitar texto
salvar arquivo
```

Código:

```python

from pywinauto import Application
from pywinauto.keyboard import send_keys

app = Application(backend="uia").start("notepad.exe")

window = app.window(title="Untitled - Notepad")

window.wait("ready")

edit = window.child_window(control_type="Edit")

edit.type_keys("Automacao profissional com Python", with_spaces=True)

send_keys("^s")

save_dialog = app.window(title="Save As")

filename = save_dialog.child_window(control_type="Edit")

filename.type_keys("teste.txt")

save_button = save_dialog.child_window(title="Save", control_type="Button")

save_button.click()

```

## Conceito mais importante deste nível

Automação robusta depende de entender:

```bash
UI TREE
```

Toda Interface Windows possui uma árvore.

```bash
Application
   Window
      Control
         SubControl
```

Se você dominar essa árvore, consegue automatizar qualquer software desktop.

