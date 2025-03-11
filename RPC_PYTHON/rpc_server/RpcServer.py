from xmlrpc.server import SimpleXMLRPCServer
import os 
import sys

# configurando o ambiente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class RpcServer():
    
    def __init__(self, ip_server: str, port_server: int):
        self.__ip = ip_server  # Encapsulamento privado
        self.__port = port_server  # Encapsulamento privado

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
    ip = "127.0.0.1"
    port = 8080

    rpc_server = RpcServer(ip, port)
    print(f"IP configurado: {rpc_server.get_ip()}")  # Brincando com o getter
    print(f"Porta configurada: {rpc_server.get_port()}") 

    rpc_server.set_ip("localhost")  # Brincando com o setter
    rpc_server.set_port(6025)
    
    print(f"IP configurado: {rpc_server.get_ip()}")  # Brincando com o getter
    print(f"Porta configurada: {rpc_server.get_port()}")
    
    # brincando com o método somar que é publico
    print(f'O resultado da soma é: {rpc_server.somar(10,20)}')
    
    rpc_server.start_server()  # Inicia o servidor
