from xmlrpc.client import ServerProxy # essa classe cria um proxy para o servidor
import sys
import os

# Configurando o caminho para incluir o diretório RPC_PYTHON para o interpretador
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rpc_server')))

# Criação do cliente
class RpcClient:
    def __init__(self, server_url: str):
        self.__proxy = ServerProxy(server_url)  # Cria um proxy XML-RPC para o servidor
    
    # Agora todos os métodos chamam o servidor remoto
    def somar(self, a, b):
        return self.__proxy.somar(a, b)  # Chama o método remoto do servidor

    def subtrair(self, a, b):
        return self.__proxy.subtrair(a, b)  # Chama o método remoto do servidor

    def multiplicar(self, a, b):
        return self.__proxy.multiplicar(a, b)  # Chama o método remoto do servidor

    def dividir(self, a, b):
        return self.__proxy.dividir(a, b)  # Chama o método remoto do servidor
        
    def get_proxy(self):
        return f"Proxy se comunicando com o servidor: {self.__proxy}"  # Retorna o proxy para depuração

if __name__ == "__main__":
    # Criando uma instância do cliente
    proxy = RpcClient(f'http://127.0.0.1:8080/')

    # Teste de comunicação com o servidor
    proxy.get_proxy()  # Apenas imprime uma mensagem para depuração

    # Fazendo chamadas ao servidor
    try:
        resultado_soma = proxy.somar(10, 20)
        print(f'O resultado da soma é: {resultado_soma}')

        resultado_subtracao = proxy.subtrair(30, 15)
        print(f'O resultado da subtração é: {resultado_subtracao}')

        resultado_multiplicacao = proxy.multiplicar(5, 6)
        print(f'O resultado da multiplicação é: {resultado_multiplicacao}')

        resultado_divisao = proxy.dividir(10, 2)
        print(f'O resultado da divisão é: {resultado_divisao}')
    
    except Exception as e:
        print(f"Erro ao se comunicar com o servidor: {e}")
