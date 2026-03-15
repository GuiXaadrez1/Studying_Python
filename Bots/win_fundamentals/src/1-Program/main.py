# Nosso primeiro programa de fundamentos ao usar essa Lib PyWinAuto

'''
    Importando lib nativa do python
'''
import time
import os 
import sys 

'''
    Importando lib para materializar o objeto de Applicacao...
'''

from pywinauto.application import Application

# inicializando nossa aplicaco pywinauto "Objeto" 
# com o motor de automacao UIA -> UI (User Interface) Automation
# para iniciar o programa do bloco de notas...

# 1. Inicializando com o backend moderno para automacao...
app: Application = Application(backend="uia").start("notepad.exe")

# 2. Aguarda um breve momento para o Windows renderizar a nova janela
time.sleep(2)

# Para debugar 
#app.windows() # Isso retorna uma lista de todas as janelas do processo
#print([win.window_text() for win in app.windows()])

# 3 - Como notpad.exe nao é mais um simples programa, vamos nos conectar
# a uma instância aberta... Ou seja, iniciamos o programa e nos conectamos 
# a uma instância aberta do programa... 
# CONECTA ao Bloco de Notas que acabou de ser aberto
# Aqui buscamos qualquer processo chamado 'notepad.exe' que tenha uma janela
app = Application(backend="uia").connect(path="notepad.exe")


# 2. Acessando janela - Agora o 'app' está realmente vinculado à janela ativa
janela_bloco_notas = app.window(title_re=".*Bloco de notas.*")

# print(janela_bloco_notas)

# 4. Aguardar a janela ser totalmente renderizada até 10 segundos...
janela_bloco_notas.wait('visible', timeout=10)

# print("Janela encontrada!")

# sys.exit(0) # para testes!

# 4. Localizando o editor - componente filho da janela...
# No Windows 11, o controle de texto costuma ser do tipo "Document" ou "RichEditD2DPT"
# Tente buscar apenas pelo control_type primeiro, que é mais certeiro:
edit_text = janela_bloco_notas.child_window(control_type="Document")

# Se o de cima falhar, tente este (comum em versões específicas):
# edit_text = janela_bloco_notas.child_window(auto_id="ContentTextArea", control_type="Edit")

edit_text.wait('ready', timeout=10)

time.sleep(1)

# Selecionar tudo (Control + A) e Copiar (Control + C)
# O caractere '^' representa a tecla CTRL
edit_text.type_keys("^a", pause=0.1) 
time.sleep(0.5)

# Excluir tudo
# A tecla Backspace é representada por {BACKSPACE} ou {BKSP}
edit_text.type_keys("{BACKSPACE}", pause=0.1)
time.sleep(0.5)

# 5. Escrevendo no editor de texto do bloco de notas...
# colocando um pause para nao escrever estranho
edit_text.type_keys("Automacao com Python", with_spaces=True, pause=0.05)

close_win = janela_bloco_notas.child_window(title="Fechar")

close_win.wait("visible",timeout=2)

close_win.click()