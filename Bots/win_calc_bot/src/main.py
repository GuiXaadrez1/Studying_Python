
'''
    BIBLIOTECAS EXTERNAS
'''

from pywinauto import Desktop
from pywinauto.mouse import click
from pywinauto.keyboard import send_keys

'''
    BIBLIOTECAS NATIVAS
'''

import sys #
import os # manipulacao de sistema operacional e diretorios
import time # manipucao de tempo do proprio computador
from logging import Logger # para criar logs profissionais 
from subprocess import Popen # para manipulacao de processos e subprocessos

'''
    DEFININDO CONSTANTES INICIAS
'''

# pegando o diretório principal/Base de onde esse script esta sendo executado
BASE_DIR:str = os.path.join(os.getcwd()) 

# pegando o caminho absoluto relativo a execucao do nosso projeto!
ROOT_PROJECT:str = os.path.abspath(os.path.join(BASE_DIR,__file__,'..','..')) 

PATH_DOC:str = os.path.join(ROOT_PROJECT,"doc")

IDENTIFICADO_ELEMENT:str = "Identificandor_elementos.txt"

'''
    Definido lógica por funcoes do nosso codigo
'''

def isExistPathDoc(path:str=PATH_DOC)->None|bool:
    """
        valida se o caminho para a pasta de documentacao existe...
        Se nao existir, irá criar uma nova
    """
    
    if not os.path.exists(path):
        
        os.makedirs(path)
        
        return None
    else:
        return True


def plusInCalc(numOne:str,numTwo:str)->None:

    try:    
       
        dialog.wait("ready")
        
        # digintando o numero
        dialog.type_keys(numOne,pause=0.1)
        
        dialog.Mais.wait("ready")
        dialog.Mais.click()
        
        dialog.type_keys(numTwo,pause=0.1)
        
        dialog.Button23.wait("ready")        
        dialog.Button23.click()
    
    except Exception as err:
        print(f"Aconteceu um erro inesperado: {err}") 
      
'''
    INICINADO LOGICA DO NOSSO CODIGO
'''

# Fazendo o usuário escolher os numeros que sera calculados...

numOne:str = input("Digite o primeiro numero que deseja somar: ")
numTwo:str = input("Digite o segundo numero: ")

# abrindo o executavel da calculador 
Popen("calc.exe",shell=True)

# Aqui estamos acessando a calculadora do windows...
dialog = Desktop(backend='uia').Calculator

# espera a calculador ficar visivel!
dialog.wait('visible')

# mostrar todos os metodos, Constantes que podemos usar no nosso objeto Desktop do Windows...
#print(dir(dialog))

if isExistPathDoc() == False:

    dialog.print_control_identifiers(filename="Identificandor_elementos.txt")

plusInCalc(numOne,numTwo)

# fecha calculadora

dialog.Button3.wait("ready")

# time.sleep(5)

dialog.Button3.click()