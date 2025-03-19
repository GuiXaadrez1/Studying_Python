from xmlrpc.client import ServerProxy  # Importa a classe para criar um proxy para o servidor
import sys
import os

# Configurando o caminho para incluir o diretório do servidor RPC
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rpc_server')))

# Criação do cliente
class RpcClient:
    def __init__(self, server_url: str):  # Construtor corrigido
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
    
    def porcentagem(self, a, b):
        return self.__proxy.porcentagem(a,b)
    
    def potenciacao(self, a, b):
        return self.__proxy.potenciacao(a, b)
    
    def radicacao(self, a): 
        return self.__proxy.radicacao(a)
    
    def fibonacci(self, n):
        return self.__proxy.fibonacci(n)

    def get_proxy(self):
        return f"Proxy se comunicando com o servidor: {self.__proxy}"  # Retorna o proxy para depuração

if __name__ == "__main__":  
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
            print("5 - Porcentagem")
            print("6 - Potenciação")
            print("7 - Radiciação")
            print("8 - Sequência de Fibonacci")
            print("9 - Realizar todas as operações (não recomendada)")

            opcao = int(input("\nDigite o número da operação matemática: "))

            if opcao not in [1, 2, 3, 4, 5, 6, 7, 8,9]:
                raise ValueError("Opção inválida! Escolha um número entre 1 e 8.")
            break  # Sai do loop se a opção for válida

        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.\n")

    if opcao == 5:
        print("\nO primeiro número é a porcentagem de um número que deseja saber a porcentagem\nExemplo: 40 = 40% -> 0.4")
        print("\nO segundo número é o número que iremos calcular a porcentagem informada!")
        
        num1 = int(input("\nDigite o primeiro quanitdade de porcentagem: "))
        num2 = int(input("Digite o segundo número para o cálculo: "))
    
    elif opcao == 6:
        print("\nNa potenciação, o primeiro número é a base e o segundo é o expoente!")
        num1 = int(input("\nDigite o primeiro número para o cálculo: "))
        num2 = int(input("Digite o segundo número para o cálculo: "))
    
    elif opcao == 7:
        num1 = int(input("\nDigite apenas o número que deseja obter a raiz quadrada: "))
    
    elif opcao == 8:
        num1 = int(input("\nDigite apenas o número que deseja verificar na sequência de Fibonacci: "))
    
    elif opcao not in [1,2,3,4,5,6,7,8,9]:
        num1 = int(input("\nDigite o primeiro número para o cálculo: "))
        num2 = int(input("Digite o segundo número para o cálculo: "))
    
    else:
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
            resultado = proxy.porcentagem(num1,num2)
            print(f'O resultado é: {resultado}%')
            
        elif opcao == 6:
            resultado = proxy.potenciacao(num1, num2)
            print(f'O resultado da potência é: {resultado}')
        
        elif opcao == 7:
            resultado = proxy.radicacao(num1)  # Corrigido para passar apenas um argumento
            print(f'O resultado da radiciação é: {resultado}')
        elif opcao == 8:
            resultado = proxy.fibonacci(num1)
            if resultado:
                print(f"\n{num1} pertence à sequência de Fibonacci.")
            else:
                print(f"\n{num1} não pertence à sequência de Fibonacci.")
        elif opcao == 9:
            print(f'O resultado da soma é: {proxy.somar(num1, num2)}')
            print(f'O resultado da subtração é: {proxy.subtrair(num1, num2)}')
            print(f'O resultado da multiplicação é: {proxy.multiplicar(num1, num2)}')
            print(f'O resultado da divisão é: {proxy.dividir(num1, num2)}')
            print(f'O resultado é: {proxy.porcentagem(num1, num2)}%')
            print(f'O resultado da potenciação é: {proxy.potenciacao(num1, num2)}')
            print(f'O resultado da radiciação do primeiro número é: {proxy.radicacao(num1)}')
            print(f'O resultado da radiciação do segundo número é: {proxy.radicacao(num2)}')
            print(f'O resultado da sequência de fibonacci do primeiro número é: {proxy.fibonacci(num1)}')
            print(f'O resultado da sequência de fibonacci do segundo número é: {proxy.fibonacci(num2)}')

    except Exception as e:
        print(f"Erro ao se comunicar com o servidor: {e}")
