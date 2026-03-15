# Vamos criar um bot que acessa o whatzap (desde que já esteja logado)
# dispara mensagens para um numero em específico


'''
    Importando a bibliotecas!
'''

from pywinauto.application import Application

import sys 
import os 

# colocando o script para ter acesso a módulos externos...
sys.path.append(os.path.abspath(os.path.join(os.getcwd(),__file__,'..')))

# importando o nosso módulo de validacao
from utils.processExecution import process_is_running,get_pid_process_running

PATH_CHORME_EXE:str = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Aplicando lógica de orquestracao de fluxo!

# se o chorme nao estiver em execucao
if not process_is_running(PATH_CHORME_EXE):
    
    # iniciamos um novo objeto pywinauto
    # Para o PyWinAuto enxergar os elementos internos (como a barra do YouTube), você precisa garantir que o Chrome foi iniciado com a flag de acessibilidade.
    app:Application = Application(backend='uia').start(PATH_CHORME_EXE + " --force-renderer-accessibility")

    # Esperando o cpu terminar de fazer as execucoes do programa...
    app.wait_cpu_usage_lower()

    # identificando a janela principal
    main_widows = app.window(control_type="Window")

    # esperando a janela ficar pronta em um tempo de até 10 segundos...
    main_widows.wait('ready',timeout=10)

    # identificando a barra de pesquisa, pelo seu AutomatizationId
    barra_pesquisa = main_widows.window(auto_id="view_1012")

    # esperando a barra ficar prontra em até 10 segundos..
    barra_pesquisa.wait("ready",10)

    # vou deixar youtube por enquanto...
    
    # digitando o nome do youtube...
    barra_pesquisa.type_keys("youtube.com.br",pause=0.01)
    
    # clicando em ENTER para abrir a página do YouTube
    barra_pesquisa.type_keys("{ENTER}")    
    
else:
    try:
        # 1. Conexão direta pela Janela que o log confirmou existir
        app = Application(backend='uia').connect(title_re=".*YouTube - Google Chrome.*", timeout=10)
        
        # 2. Captura a janela
        chrome_window = app.window(title_re=".*YouTube - Google Chrome.*")
        
        # 3. TRUQUE: Trazer a janela para frente ANTES de buscar o filho
        # Isso força o Chrome a renderizar a árvore de acessibilidade UIA
        chrome_window.set_focus()
        
        # 4. Busca o campo de busca
        # Aplicando Regex para deixar mais flexivel a busca pela arvore de componentes UIA...
        campo_busca = chrome_window.child_window(
            title_re=".*Pesquisar.*", 
            control_type="ComboBox", 
            depth=None
        )
        
        # Aguarda o elemento estar pronto para interação física
        campo_busca.wait('visible', timeout=15)
        
        # 5. Interação com o Mouse (click_input é mais real que click)
        campo_busca.click_input()
        
        # 6. Limpeza e Digitação
        # Usamos ^a{BACKSPACE} para garantir que o campo esteja vazio
        campo_busca.type_keys("^a{BACKSPACE}", pause=0.05)
        campo_busca.type_keys("Curso PHP", with_spaces=True, pause=0.05)
        campo_busca.type_keys("{ENTER}")
            
        print("✅ Pesquisa realizada com sucesso!")
    
    except Exception as e:
        
        print(f"❌ Erro ao conectar ou localizar: {e}")
        
        # Se falhar, vamos tentar ver QUEM o PyWinAuto está encontrando
        # Isso ajuda a debugar se o título da aba mudou
        from pywinauto import Desktop
        
        print("Janelas visíveis no Windows agora:")
        
        for w in Desktop(backend="uia").windows():
            if "Chrome" in w.window_text():
                print(f"-> {w.window_text()}")