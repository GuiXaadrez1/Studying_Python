import random 
from tkinter import messagebox
import subprocess
import sys
import os

def iniciar_programa(caminho_programa):
    
    try:
        subprocess.run([sys.executable, caminho_programa], check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(-1)
                
def sortear(lista) -> list:
    
    print('--------------------')
    print('| SORTEANDO A MESA |')

    print('--------------------')
    
    nova_lista = []
    for i in random.choice(lista):
        elemento = random.choice(lista)
        nova_lista.append(elemento)
        print(elemento)
    
    print(f'{elemento} <-- FOI SORTEADO')         
    
    mensagem_alerta = messagebox.showwarning('RESULTADO', f'\nA MESA ATUAL É: {elemento}\n\nProbabilidade de cair a carta no sorteio: 33,33%')        
    pergunta_reiniciar = messagebox.askyesno('SORTEAR','SORTEAR NOVAMENTE?')
    
    if pergunta_reiniciar:
        iniciar_programa(os.path.join(os.getcwd(),'game_lairs.py'))
    else:
        sys.exit(-1)
                
    return mensagem_alerta 

if __name__ == '__main__':
    
    tables = ['ACES_TABLE','KINGS_TABLE','QUEEN_TABLE']
    print(sortear(tables))
