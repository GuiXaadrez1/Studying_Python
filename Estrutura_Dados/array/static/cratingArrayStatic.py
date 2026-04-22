import numpy as np

class StaticArray:
    
    """
        Simula o comportamento de um Array Estático usando a biblioteca NumPy.

        Um array estático é uma estrutura de dados linear cujo tamanho é definido
        no momento da criação e não pode ser alterado posteriormente. Todos os
        elementos são armazenados em posições de memória contíguas, permitindo
        acesso direto via índice em tempo constante O(1).

        Por padrão, ao instanciar o objeto, todas as posições do array são
        inicializadas com o valor `None`, representando células de memória
        alocadas porém ainda não preenchidas.

        Características:
        
            - Tamanho fixo definido na instanciação.
            - Indexação baseada em zero (0 até length - 1).
            - Acesso a qualquer elemento em tempo O(1).
            - Não permite redimensionamento após a criação.

        Args:
            length (int): Quantidade de posições que o array deve reservar.

        Example:
        
            >>> sa = StaticArray(5)
            >>> print(sa.getFirstElement())
            Primeiro elemento na posicao 0: None
            >>> print(sa.getLastElement())
            Ultimo elemento do array: None
    """

    def __init__(self, length: int):
        
        # Contante que define o tamanho do array
        self._LENGTH = length
        
        # contante que cria o array com base no seu tamanho porem com elementos vazios
        self._arrayElements:np.ndarray = np.array([None] * self._LENGTH)

    def getFirstElement(self) -> int | str:
        """Obtendo o primeiro elemento do Array acessando o índice 0"""
        return f"Primeiro elemento: {self._arrayElements[0]}"
    
    def getLastElement(self) -> int | str:
        """
            Obtendo o último elemento do Array
            respeitando o conceito: n-1
        """
        return f"Ultimo elemento do array: {self._arrayElements[self._LENGTH - 1]}"


if __name__ == "__main__":
    
    staticArray = StaticArray(10)
    #print(staticArray.getFirstElement())
    #print(staticArray.getLastElement())
    
    # interando sobre os elementos do array statico    
    for i,elemnt in enumerate(staticArray._arrayElements):
        print(f"índicie:{i} --> valor_elemento_array: {elemnt}")