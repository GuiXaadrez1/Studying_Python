import sys
import os

# Configurando o caminho para incluir o diretório RPC_PYTHON para o interpretador Ler
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rpc_server')))
print(sys.path[-1]) # puxando o último item

# como já adcionei a subpasta rpc_server no sys.path, posso realizar importação direta
from RpcServer import RpcServer
 

# Criação do cliente
class RpcClient:
    def __init__(self):
        pass

# Testando a criação do cliente
client = RpcClient()
print("Cliente criado com sucesso!")
