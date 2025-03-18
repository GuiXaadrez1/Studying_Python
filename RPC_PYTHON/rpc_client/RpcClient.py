from xmlrpc.client import ServerProxy  # Importa a classe para criar um proxy para o servidor
import sys
import os

# Configurando o caminho para incluir o diretório do servidor RPC
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rpc_server')))

# Criação do cliente
class RpcClient:
    def __init__(self, server_url: str):  # Corrigido para __init__
        self.__proxy = ServerProxy(server_url)  # Cria um proxy XML-RPC para o servidor
    
    # Métodos remotos chamando o servidor
    def somar(self, a, b):
        return self.__proxy.somar(a, b)

    def subtrair(self, a, b):
        return self.__proxy.subtrair(a, b)

    def multiplicar(self, a, b):
        return self.__proxy.multiplicar(a, b)

    def dividir(self, a, b):
        return self.__proxy.dividir(a, b)

    def get_proxy(self):
        return f"Proxy se comunicando com o servidor: {self.__proxy}"  # Retorna o proxy para depuração

if __name__ == "__main__":  # Corrigido para "__main__"
    # Criando uma instância do cliente
    proxy = RpcClient('http://127.0.0.1:8080/')

    # Teste de comunicação com o servidor
    print(proxy.get_proxy())  # Agora imprime corretamente

    while True:
        try:
            # Menu de opções
            print("\nEscolha uma operação matemática:")
            print("1 - Somar")
            print("2 - Subtrair")
            print("3 - Multiplicar")
            print("4 - Dividir")
            print("5 - Realizar todas as operações")

            opcao = int(input("\nDigite o número da operação matemática: "))

            if opcao not in [1, 2, 3, 4, 5]:
                raise ValueError("Opção inválida! Escolha um número entre 1 e 5.")
            break  # Sai do loop se a opção for válida

        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.\n")

    # Pegando números do usuário
    num1 = int(input("\nDigite o primeiro número para o cálculo: "))
    num2 = int(input("Digite o segundo número para o cálculo: "))

    # Chamadas ao servidor
    try:
        if opcao == 1:
            resultado = proxy.somar(num1, num2)
            print(f'O resultado da soma é: {resultado}')
        elif opcao == 2:
            resultado = proxy.subtrair(num1, num2)
            print(f'O resultado da subtração é: {resultado}')
        elif opcao == 3:
            resultado = proxy.multiplicar(num1, num2)
            print(f'O resultado da multiplicação é: {resultado}')
        elif opcao == 4:
            resultado = proxy.dividir(num1, num2)
            print(f'O resultado da divisão é: {resultado}')
        elif opcao == 5:
            print(f'O resultado da soma é: {proxy.somar(num1, num2)}')
            print(f'O resultado da subtração é: {proxy.subtrair(num1, num2)}')
            print(f'O resultado da multiplicação é: {proxy.multiplicar(num1, num2)}')
            print(f'O resultado da divisão é: {proxy.dividir(num1, num2)}')

    except Exception as e:
        print(f"Erro ao se comunicar com o servidor: {e}")
