import numpy as np
import sys

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

    def __init__(self, length: int, typecode:str|int|float|bool):
        
        # Constante que define o comprimento do array (espaços livres ou não)
        self.__LENGTH = length
        
        # Flag que restringe o array a um único tipo de dado.
        # No conceito mais fundamental, arrays são homogêneos —
        # todas as posições devem armazenar o mesmo tipo.
        self.__TYPEARRAY = typecode 
         
        # Atributos padrão da classe que define o tamanho inicial do array
        # ou seja, espaços preenchidos
        self._size = 0
        
        # contante que cria o array com base no seu tamanho porem com elementos vazios
        self.__arrayElements:np.ndarray = np.array([None] * self.__LENGTH)

    def getFirstElement(self):
        """Obtendo o primeiro elemento do Array acessando o índice 0"""
        return f"Primeiro elemento: {self.__arrayElements[0]}"
    
    def getLastElement(self):
        """
            Obtendo o último elemento do Array
            respeitando o conceito: n-1
        """
        return f"Ultimo elemento do array: {self.__arrayElements[self.__LENGTH - 1]}"

    def insertValueElement(self,new_value)->None|str:
        
        if self._size >= self.__LENGTH:
            raise ValueError('This array is full')
        else:
                
            if type(new_value) is type(self.__TYPEARRAY):
                self.__arrayElements[self._size] = new_value
                self._size += 1
            else:
                raise TypeError("Typecode element not equal the typecode Array")
                
    def removeElemnt(self)->None:
        
        """
        Remove um elemento do array estático
        
        Raises:
            ValueError: _description_
        """
        if self._size == 0:
            raise ValueError('O array está vazio!')
        else:
            
            self.__arrayElements[self._size - 1] = None
            self._size -=1 
    
    def traverse(self,callback:callable):
        """
            Percorre todos os elementos do array aplicando uma função de callback.

            A operação de travessia (traversal) é uma das operações fundamentais
            em estruturas de dados lineares. Ela consiste em visitar sistematicamente
            cada elemento exatamente uma vez, do índice 0 até n-1, sem modificar
            a estrutura subjacente.

            O parâmetro `callback` segue o padrão de projeto conhecido como
            higher-order function — uma função que recebe outra função como argumento.
            Isso permite desacoplar a lógica de iteração da lógica de processamento,
            tornando o método reutilizável para qualquer operação: impressão,
            transformação, filtragem, acumulação, etc.

            Complexidade:
                - Tempo:  O(n) — cada elemento é visitado exatamente uma vez.
                - Espaço: O(1) — nenhuma estrutura auxiliar é criada.

            Args:
                callback (callable): Função aplicada a cada elemento durante
                a travessia. Deve aceitar um único argumento correspondente
                ao valor do elemento na posição atual.

            Example:
                >>> sa = StaticArray(5, int())
                >>> sa.insertValueElement(10)
                >>> sa.insertValueElement(20)
                >>> sa.traverse(callback=print)
                10
                20
                None
                None
                None
            """
        
        for index,element in enumerate(staticArray.__arrayElements):
            
            # usando uma função de chamada(retorno)
            callback(element)      
    
    def sortArray(self):
        pass
    
if __name__ == "__main__":
    
    # Array homogêneo de strings, alocado e vazio.
    # Classificado como UnSortedArray pois os elementos
    # serão inseridos sem critério de ordenação.
    staticArray = StaticArray(10,str())
    
    # pegando o primeiro e ultimo valor dos elementos do array
    print(staticArray.getFirstElement())
    print(staticArray.getLastElement())
    
    # inserindo seis valores no array    
    for i in range(5):
        staticArray.insertValueElement("hellow")
        # staticArray.insertValueElement(10)
      
    # removendo tres elementos do array
    for i in range(3):
        staticArray.removeElemnt()
    
    # iterando sobre o array e printa o valor do elemento
    staticArray.traverse(print)
    
    print("Tamanho atual do array com elementos preenchidos:",staticArray._size)