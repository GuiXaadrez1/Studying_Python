from logging import exception

def fibonacci(n):
    t1, t2 = 1, 1  # criando tupla (1,1)
    try:
        while True:
            t1, t2 = t2, t1 + t2  # t1 e t2 são termos
            print(t1,end=" ")
            if t1 == n:
                return True
                break
            elif t1 > n:  # adicionando uma condição de parada para evitar loop infinito
                print("\nNão existe esse número na sequência de Fibonacci.")
                return False
                break
    except Exception as e:
        print(f"Tente novamente, ocorreu o erro: {e}")

while True:
    try:
        n = int(input("Digite o número da sequência de Fibonacci que deseja encontrar: "))
        if fibonacci(n):
            print(f"\n{n} existe na sequência de Fibonacci.")
            break
        else:
            print(f"{n} não existe na sequência de Fibonacci. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")