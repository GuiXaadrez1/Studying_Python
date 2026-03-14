# Aqui vamos aprender alguns fundamentos de pywinauto na prática
# primiero vamos começar com aplicacoes que nao sao externas ao windows...
# por exemplo: notpad..., vscode e etc...
 
from pywinauto.application import Application

# inicializando nossa aplicaco pywinauto "Objeto"
app:Application = Application.start("notepad.exe") 
