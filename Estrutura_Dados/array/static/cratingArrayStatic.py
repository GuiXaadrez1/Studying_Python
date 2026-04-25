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

    def __init__(
        self, 
        length: int,
        typecode:str|int|float|bool|np.ndarray,
        values:np.ndarray|None=None
    ):
        
        # Constante que define o comprimento do array (espaços livres ou não)
        self.__LENGTH = length
        
        # Flag que restringe o array a um único tipo de dado.
        # No conceito mais fundamental, arrays são homogêneos(aceitam apenas um tipo de dado)
        # todas as posições devem armazenar o mesmo tipo.
        self.__TYPEARRAY = typecode 
         
        # Atributos padrão da classe que define o tamanho inicial do array
        # ou seja, espaços preenchidos
        self._size = 0
        
        # contante que cria o array com base no seu tamanho porem com elementos vazios
        self.__arrayElements:np.ndarray = np.array([None] * self.__LENGTH)

    # Dunder method (magic method) — método especial do Python identificado
    # pelo duplo underscore antes e depois do nome (__método__).
    # Não é chamado diretamente — o Python o invoca implicitamente
    # quando a função nativa len() é aplicada sobre o objeto.
    #
    # Retorna apenas os elementos válidos do array através de _size,
    # ignorando as posições vazias (None) sem precisar percorrer
    # ou modificar o array — _size já é mantido atualizado por
    # todos os métodos de inserção e remoção da classe.
    #
    # Exemplo:
    #   capacidade total:  ["a", "b", None, None, None, None, None, None]
    #   len(staticArray)   → 2  (apenas elementos válidos) ✅
    #   staticArray._size  → 2  (mesma fonte de verdade)'
    #
    # Complexidade:
    #   O(1) — acesso direto ao atributo _size, sem iteração.
    def __len__(self):
        return self._size
    
    def __str__(self):
        # Dunder method que controla a representação do objeto como string.
        # Chamado implicitamente pelo Python quando se usa print() ou str().
        # Sem ele, print(staticArray) exibiria o endereço de memória do objeto.
        # Retorna o ndarray completo — incluindo as posições vazias (None) —
        # permitindo visualizar a estrutura real alocada em memória.
        #
        # Exemplo:
        #   print(staticArray) → ["a" "b" None None None None None None]
        return str(self.__arrayElements)
    
    def __iter__(self):
        # Dunder method que torna o objeto iterável.
        # Chamado implicitamente pelo Python em loops for e
        # funções como list(), tuple(), etc.
        # Itera apenas sobre os elementos válidos (_size),
        # ignorando as posições vazias (None).
        #
        # Exemplo:
        #   for element in staticArray:
        #       print(element)  ← percorre só os válidos
        for index in range(self._size):
            
            yield self.__arrayElements[index]
            
            # O yield em Python é usado dentro de uma função para transformá-la
            # em um gerador.  Ao invés de retornar um único valor e encerrar a função
            # como o return, o yield pausa a execução da função, retorna um valor e mantém
            # seu estado (como os valores das variáveis locais).  
            # Na próxima vez que o gerador for iterado, a função retoma exatamente
            # de onde parou, logo após o yield.

    def __getitem__(self, idx: int):
        # Dunder method que permite acesso por índice via colchetes.
        # Chamado implicitamente pelo Python quando se usa array[idx].
        # Respeita o intervalo válido [0, _size-1], ignorando
        # as posições vazias (None).
        #
        # Exemplo:
        #   staticArray[0]  → primeiro elemento válido
        #   staticArray[2]  → terceiro elemento válido
        #
        # Raises:
        #   IndexError: Se o índice estiver fora do intervalo válido.
        if idx < 0 or idx >= self._size:
            raise IndexError(f'Índice {idx} fora do intervalo válido [0, {self._size - 1}].')
        return self.__arrayElements[idx]
        
    def getFirstElement(self):
        # Retorna o primeiro elemento do array acessando diretamente
        # o índice 0 — operação O(1) por acesso via índice fixo.
        return f"Primeiro elemento: {self.__arrayElements[0]}"

    def getLastElement(self):
        # Retorna o último elemento alocado do array acessando
        # o índice LENGTH-1, respeitando o conceito n-1 da
        # indexação base zero — operação O(1).
        # Atenção: retorna a última posição ALOCADA, não o último
        # elemento válido. Para o último válido, use _size-1.
        return f"Ultimo elemento do array: {self.__arrayElements[self.__LENGTH - 1]}"

    def insertValueElement(self, new_value) -> None:
        """
        Insere um novo elemento na próxima posição disponível do array estático.

        Acessa diretamente a primeira posição livre através de _size,
        insere o valor e incrementa o tamanho lógico. A inserção sempre
        ocorre no final dos elementos válidos, preservando a ordem de
        inserção dos demais.

        A homogeneidade do array é garantida pela validação do tipo do
        valor inserido contra o typecode definido na instanciação —
        qualquer tipo divergente é rejeitado com TypeError.

        Exemplo:
            antes:  [1, 2, 3, None, None, None]  _size=3
            inserir valor 4:
            depois: [1, 2, 3, 4, None, None]  _size=4

        Complexidade:
            - Tempo:  O(1) — acesso direto via índice _size.
            - Espaço: O(1) — nenhuma estrutura auxiliar criada.

        Args:
            new_value: Valor a ser inserido. Deve ser do mesmo tipo
            definido pelo typecode na instanciação do array.

        Raises:
            ValueError: Se o array estiver cheio (_size >= LENGTH),
            pois arrays estáticos não permitem redimensionamento.
            TypeError: Se o tipo do valor inserido divergir do typecode
            definido, violando a homogeneidade do array.
        """
        if self._size >= self.__LENGTH:
            raise ValueError('This array is full')

        if type(new_value) is type(self.__TYPEARRAY):
            self.__arrayElements[self._size] = new_value
            self._size += 1
        else:
            raise TypeError("Typecode element not equal the typecode Array")
                
    def removeLastElement(self) -> None:
        """
        Remove o último elemento válido do array estático.

        Acessa diretamente a última posição ocupada através de _size-1,
        substitui o valor por None e decrementa o tamanho lógico.
        Não há deslocamento de elementos — apenas a última posição
        é limpa, preservando a ordem de todos os demais.

        Exemplo:
            antes:  [1, 2, 3, 4, 5, None, None, None]  _size=5
            depois: [1, 2, 3, 4, None, None, None, None]  _size=4

        Complexidade:
            - Tempo:  O(1) — acesso direto via índice _size-1.
            - Espaço: O(1) — nenhuma estrutura auxiliar criada.

        Raises:
            ValueError: Se o array estiver vazio (_size == 0),
            pois não há elemento válido para remover.
        """
        if self._size == 0:
            raise ValueError('O array está vazio!')

        self.__arrayElements[self._size - 1] = None
        self._size -= 1
 
    def removeElementWithIndex(self, idx: int) -> np.ndarray:
        """
        Remove um elemento do array estático pelo seu índice.

        Utiliza a estratégia de substituição(swap) pelo último elemento válido,
        operando em duas etapas:

            1. O elemento na posição `idx` é sobrescrito pelo último elemento
            válido do array (posição _size-1), preenchendo o "buraco" gerado
            pela remoção.

            2. A última posição (_size-1), que agora está duplicada, é limpa
            com None e o tamanho lógico é decrementado.

        Exemplo:
            antes:  [1, 2, 3, 4, 5, None, None, None]  _size=5
            remover idx=1 (valor 2):
            passo1: [1, 5, 3, 4, 5, None, None, None]  ← último (5) copia para idx=1
            passo2: [1, 5, 3, 4, None, None, None, None]  _size=4  ← último limpo

        Consequências:
            - O valor removido é destruído (sobrescrito).
            - O último elemento válido muda de posição.
            - A ordem original de inserção não é preservada.
            - O array retorna desordenado em relação à inserção original.

        Complexidade:
            - Tempo:  O(1) — nenhum deslocamento de elementos.
            - Espaço: O(1) — nenhuma estrutura auxiliar criada.

        Args:
            idx (int): Índice do elemento a ser removido. Deve estar
            no intervalo válido [0, size-1].

        Returns:
            np.ndarray: O array atualizado após a remoção, com a última
            posição válida limpa e _size decrementado.

        Raises:
            ValueError: Se o array estiver vazio.
            ValueError: Se o índice estiver fora do intervalo válido [0, size-1].
        """
        if self._size == 0:
            raise ValueError('Tentou deletar em um array vazio.')
        elif idx < 0 or idx >= self._size:
            raise ValueError(f'Índice {idx} fora do intervalo válido [0, {self._size - 1}].')

        self.__arrayElements[idx] = self.__arrayElements[self._size - 1]
        self.__arrayElements[self._size - 1] = None
        self._size -= 1

        return self.__arrayElements
     
    def maxElementIntoArray(self, array: object) -> tuple:
        
        """
        Localiza o maior elemento dentro de um StaticArray e retorna
        seu índice e valor.

        Percorre todos os elementos válidos do array comparando cada um
        com o maior valor encontrado até o momento — estratégia conhecida
        como Linear Search for Maximum. O índice do maior elemento é
        atualizado sempre que um valor superior é encontrado.

        Exemplo:
            array: [3, 7, 1, 9, 2, None, None, None]  _size=5
            percorre → 3, 7, 1, 9, 2
            maior encontrado → índice=3, valor=9
            retorna → (3, 9)

        Complexidade:
            - Tempo:  O(n) — todos os elementos válidos são visitados.
            - Espaço: O(1) — nenhuma estrutura auxiliar criada.

        Args:
            array (StaticArray): Instância de StaticArray sobre a qual
            a busca pelo maior elemento será realizada.

        Returns:
            tuple: Par (índice, valor) correspondente ao maior elemento
            encontrado no array.

        Raises:
            ValueError:  Se o array estiver vazio.
            TypeError:   Se o objeto passado não for uma instância de StaticArray.
        """
        
        if not isinstance(array, StaticArray):
            raise TypeError("O objeto passado não é uma instância de StaticArray!")

        if len(array) == 0:
            raise ValueError("O array está vazio!")

        max_idx = 0

        for idx in range(array._size):
            
            if array.__arrayElements[idx] > array.__arrayElements[max_idx]:
                
                max_idx = idx

        return max_idx, array.__arrayElements[max_idx]
    
    def minElementIntoArray(self, array: object) -> tuple:
        """
        Localiza o menor elemento dentro de um StaticArray e retorna
        seu índice e valor.

        Percorre todos os elementos válidos do array comparando cada um
        com o menor valor encontrado até o momento — estratégia conhecida
        como Linear Search for Minimum. O índice do menor elemento é
        atualizado sempre que um valor inferior ou igual é encontrado.

        Exemplo:
            array: [3, 7, 1, 9, 2, None, None, None]  _size=5
            percorre → 3, 7, 1, 9, 2
            menor encontrado → índice=2, valor=1
            retorna → (2, 1)

        Complexidade:
            - Tempo:  O(n) — todos os elementos válidos são visitados.
            - Espaço: O(1) — nenhuma estrutura auxiliar criada.

        Args:
            array (StaticArray): Instância de StaticArray sobre a qual
            a busca pelo menor elemento será realizada.

        Returns:
            tuple: Par (índice, valor) correspondente ao menor elemento
            encontrado no array.

        Raises:
            ValueError: Se o array estiver vazio.
            TypeError:  Se o objeto passado não for uma instância de StaticArray.
        """
        if not isinstance(array, StaticArray):
            raise TypeError("O objeto passado não é uma instância de StaticArray!")
        if len(array) == 0:
            raise ValueError("O array está vazio!")

        min_idx = 0

        for idx in range(array._size):
            if array.__arrayElements[idx] <= array.__arrayElements[min_idx]:
                min_idx = idx

        return min_idx, array.__arrayElements[min_idx]
    
    def find(self, target) -> np.ndarray | None:
        """
        Busca um elemento no array estático pelo seu valor e retorna
        a primeira ocorrência encontrada.

        Por se tratar de um array desordenado (UnSortedArray), não é possível
        aplicar estratégias de busca eficientes como a Busca Binária, que
        exige ordenação prévia. Portanto, utiliza-se a Busca Linear (Linear Search)
        — cada elemento é visitado sequencialmente do índice 0 até _size-1
        até que a primeira ocorrência do alvo seja encontrada.

        Exemplo:
            array: ["a", "b", "c", "d", "e", None, None]  _size=5
            find("c") → percorre índices 0, 1, 2 → encontra "c" → retorna np.array(["c"])
            find("z") → percorre todos os índices → não encontra  → retorna None

        Complexidade:
            - Melhor caso:  O(1) — alvo encontrado no índice 0.
            - Pior caso:    O(n) — alvo no último índice ou inexistente.
            - Espaço:       O(1) — nenhuma estrutura auxiliar criada.

        Args:
            target: Valor a ser localizado no array. Deve ser do mesmo
            tipo definido pelo typecode na instanciação.

        Returns:
            np.ndarray com a primeira ocorrência encontrada, ou None caso
            o alvo não exista entre os elementos válidos do array.
        """
        for index in range(self._size):

            if self.__arrayElements[index] == target:
                return np.array([self.__arrayElements[index]])

        return None
    
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
        
        for index,element in enumerate(self.__arrayElements):     
            # usando uma função de chamada(retorno)
            callback(index,element)      
    
    # Aqui vamos tornar o nosso array estático e desordenado 
    # em um array estático e ordenado;
    def sortArray(self):
        pass
    
if __name__ == "__main__":
    
    # Array homogêneo de strings, alocado e vazio.
    # Classificado como UnSortedArray pois os elementos
    # serão inseridos sem critério de ordenação.
    staticArray = StaticArray(10,str())
    
    # pegando o primeiro e ultimo valor dos elementos do array ao iniciar
    print(staticArray.getFirstElement())
    print(staticArray.getLastElement())
        
    for i in range(3):
        staticArray.insertValueElement("hellow")
        
    for i in range(2):
        staticArray.insertValueElement("hello")
    
    for i in range(5):
        staticArray.insertValueElement("hell")
      
    # removendo tres elementos do array
    for i in range(2):
        staticArray.removeLastElement()
    
    # iterando sobre o array e printa o valor do elemento
    # staticArray.traverse(print)
    
    staticArray.removeElementWithIndex(5)
    print(staticArray.find("hellow"))
    
    print(staticArray)
    print(len(staticArray))    

    counters=StaticArray(50,int())
    
    for i in range(50):
        
        if counters._size <= i:
            
            counters.insertValueElement(i+1) 

    print(staticArray.maxElementIntoArray(counters))
    print(staticArray.minElementIntoArray(counters))