'''
    Funções utéis para processo em execucao
    Basicamente vamos ter todos as funcoes referente a processos 
    sub processos aqui.
'''

import subprocess
import psutil
import os 
import sys


def process_is_running(path_exe:str)->bool|list:
    
    """ Validador de execucao de processos

        Esta funcao rescebe um caminho absoluto do executavel de um programa
        valida se esta em execucao ou nao e capita o pid real
    Returns:
        list: retorna uma lista com o pid do programa em execucao e um true como indicativo
        bool: retorna false caso nao o programa nao esteja em execucao
    """
    
    # Normaliza o caminho para evitar problemas de barras / ou \
    path_exe = os.path.normcase(os.path.abspath(path_exe))
    
    # Percorre sobre uma lista de pid de executaveis...
    for proc in psutil.process_iter(['pid', 'exe']):
        
        try:
            # Verifica se o processo tem a info 'exe' e se não é None
            if proc.info['exe'] and os.path.normcase(proc.info['exe']) == path_exe:
                
                #print(f"PID do CHORME em execucao: {proc.info['pid']}")
                
                return [proc.info['pid'],True]
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue   
    
    print("processo nao esta em execucao!")
    return False # Retorno explícito caso não encontre nada

def get_pid_process_running(validatoFunction):
    
    if not validatoFunction:
        return 0
    
    if validatoFunction:
        return validatoFunction[0]
 
if __name__ == "__main__":
    
    PATH_EXE_TESTE = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    process_status = process_is_running(PATH_EXE_TESTE)
    
    print(get_pid_process_running(process_status))
