import os
import sys
import threading

# Adiciona RPC_PYTHON ao sys.path para garantir que Python consiga encontrar o pacote
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# importando as minhas classes
from rpc_server.RpcServer import RpcServer
from rpc_client.RpcClient import RpcClient

# servidor é o produto

# materializando o meu server na forma padrão
server = RpcServer()

# Criando uma thread para rodar o servidor em paralelo
server_thread = threading.Thread(target=server.start_server)
server_thread.daemon = True  # Isso faz a thread ser finalizada quando o programa principal terminar
server_thread.start()


# cliente é o produto

# Agora você pode criar o cliente enquanto o servidor está rodando
proxy = RpcClient(f'http://{server.get_ip()}:{server.get_port()}/')

# resposta do servidor
print(proxy.somar(10, 10))

# Testando o método get_proxy()
print(proxy.get_proxy())
