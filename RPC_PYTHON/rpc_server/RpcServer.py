from xmlrpc.server import SimpleXMLRPCServer
import os
import sys
import math

# Configurando o ambiente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class RpcServer:
    
    def __init__(self, ip_server: str = "127.0.0.1", port_server: int = 8080):
        self.__ip = ip_server  # Encapsulamento privado
        self.__port = port_server 
        self.start_server()  # Inicia o servidor automaticamente

    def start_server(self):
        server = SimpleXMLRPCServer((self.__ip, self.__port))  # Criando o servidor RPC
        print(f"Servidor RPC rodando no IP: {self.__ip} e na porta: {self.__port}")
        server.register_instance(self)  # Registra os métodos da classe como métodos RPC
        server.serve_forever()  # Mantém o servidor rodando indefinidamente
    
    # Métodos de cálculo (soma, subtração, multiplicação, divisão)
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero!"
        return a / b
    
    def potenciacao(self, a, b):
        return a ** b
    
    def radicacao(self, a):
        return math.sqrt(a)  # Raiz quadrada de 'a'
    
    def fibonacci(self, n):
        t1, t2 = 0, 1  # Os primeiros termos da sequência de Fibonacci

        try:
            while t1 <= n:  # Agora o loop percorre toda a sequência
                if t1 == n:
                    print(f"{n} pertence à sequência de Fibonacci.")
                    return True 
                t1, t2 = t2, t1 + t2  # Atualiza os termos de Fibonacci
            
            print(f"{n} NÃO pertence à sequência de Fibonacci.")
            return False

        except Exception as e:
            print(f"Tente novamente, ocorreu o erro: {e}")
            return False  

    # Getter para o IP
    def get_ip(self):    
        return self.__ip
    
    # Setter para o IP
    def set_ip(self, novo_ip):
        if isinstance(novo_ip, str):  # Validação
            self.__ip = novo_ip
        else:
            raise ValueError("O IP deve ser uma string!")

    # Getter para a porta
    def get_port(self):
        return self.__port
    
    # Setter para a porta
    def set_port(self, new_port):
        if isinstance(new_port, int) and 0 < new_port < 65536:  # Validação para portas válidas
            self.__port = new_port
        else:
            raise ValueError("A porta deve ser um número inteiro entre 1 e 65535!")    

if __name__ == "__main__":
    
    rpc_server = RpcServer()
    print(f"IP configurado: {rpc_server.get_ip()}")  # Testando getter
    print(f"Porta configurada: {rpc_server.get_port()}") 

    # print(f'O resultado da soma é: {rpc_server.somar(10, 20)}')  # Teste
