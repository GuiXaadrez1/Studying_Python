# Nosso primeiro programa de fundamentos ao usar essa Lib PyWinAuto

'''
    Importando lib para materializar o objeto de Applicacao...
'''

from pywinauto.application import Application

# inicializando nossa aplicaco pywinauto "Objeto" 
# com o motor de automacao UIA -> UI (User Interface) Automation
# para iniciar o programa do bloco de notas...

# 1. Inicializando com o backend correto
app: Application = Application(backend="uia").start("notepad.exe")

# 2. Usando Regex para o título (mais resiliente)
# O '.*' ignora o que vem antes ou depois de 'Bloco de Notas'
janela_bloco_notas = app.window(title_re=".*Bloco de Notas.*")

# 3. Aguardar a janela estar pronta para interação
janela_bloco_notas.wait('visible', timeout=10)

# 4. Localizando o editor
# Dica: No Bloco de Notas moderno, o controle costuma ser "RichEditD2DPT" ou "Edit"
edit_text = janela_bloco_notas.child_window(title="Editor de texto", control_type="Edit")

edit_text.wait('ready')

# 5. Escrevendo (Correção dos nomes dos métodos e parâmetros)
edit_text.type_keys("Automação com Python", with_spaces=True, with_check_line_break=True)
