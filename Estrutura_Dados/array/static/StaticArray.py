import numpy as np
import sys

class StaticArray:
    
    """
    Container de tamanho fixo com suporte a tipagem homogênea e aninhamento.

    Simula o comportamento de um Array Estático inspirado no conceito de vetores
    unidimensionais homogêneos de linguagens como C — onde o tipo de dado é definido
    na instanciação e não pode ser alterado. O tamanho é fixo e não permite
    redimensionamento após a criação.

    Suporta dois modos de operação mutuamente exclusivos:

        Modo Primitivo (Fluxo 1):
            O typecode define um tipo escalar (str, int, float, bool).
            Os valores injetados via `values` devem ser exclusivamente escalares —
            containers internos são rejeitados para preservar a homogeneidade.
            Destinado a vetores unidimensionais de elementos primitivos.

            Exemplo válido:
                StaticArray(5, str(), ['a', 'b', 'c'])
                output → ['a', 'b', 'c', None, None]

            Exemplo rejeitado:
                StaticArray(5, str(), [['a', 'b'], 'c'])
                → TypeError: containers internos não são permitidos no Modo Primitivo.

        Modo Aninhado (Fluxo 2):
            O typecode define um container (list, np.ndarray, StaticArray).
            Os valores injetados via `values` devem ser exclusivamente containers —
            escalares internos são rejeitados para preservar a homogeneidade.
            Destinado a estruturas multidimensionais de tamanho fixo,
            onde cada elemento do array é ele mesmo um container,
            simulando o comportamento de uma matriz estática.

            Exemplo válido:
                StaticArray(2, list(), [['a', 'b'], ['c', 'd']])
                output → [['a', 'b'], ['c', 'd']]

            Exemplo rejeitado:
                StaticArray(2, list(), [['a', 'b'], 'c'])
                → TypeError: escalares internos não são permitidos no Modo Aninhado.

    Características:

        - Tamanho fixo definido na instanciação.
        - Tipagem homogênea — aceita apenas um tipo de dado por instância.
        - Indexação baseada em zero (0 até length - 1).
        - Acesso a qualquer elemento em tempo O(1).
        - Não permite redimensionamento após a criação.
        - Suporta estruturas unidimensionais (Modo Primitivo) e
        multidimensionais de tamanho fixo (Modo Aninhado).
        - Iterável via protocolo Python (__iter__, __getitem__).

    Args:
        length   (int): Quantidade de posições a reservar na memória.
        typecode (str | int | float | bool | list | np.ndarray | object):
                Tipo de dado aceito pelo array. Define a homogeneidade
                e o modo de operação:
                - Escalar (str, int, float, bool) → Modo Primitivo
                - Container (list, np.ndarray, StaticArray) → Modo Aninhado
        values   (list | np.ndarray | StaticArray | None): Valores iniciais
                opcionais a serem injetados na instanciação.
                - Modo Primitivo: apenas escalares são permitidos internamente.
                - Modo Aninhado: apenas containers são permitidos internamente.

    Raises:
        MemoryError: Se o número de valores em `values` exceder o `length` alocado.
        TypeError:   Se no Modo Primitivo algum elemento interno for um container,
                    ou se no Modo Aninhado algum elemento interno for um escalar.

    Example:

        >>> # Modo Primitivo — vetor unidimensional
        >>> sa = StaticArray(5, str(), ['a', 'b', 'c'])
        >>> print(sa)
        ['a' 'b' 'c' None None]

        >>> # Modo Aninhado — matriz estática
        >>> sa_matriz = StaticArray(2, list(), [['x', 'y'], ['z', 'w']])
        >>> print(sa_matriz)
        [list(['x', 'y']) list(['z', 'w'])]
    """

    def __init__(
        self, 
        length: int,
        typecode: str|int|float|bool|list|np.ndarray|object,
        values: object|list|np.ndarray|None=None
    ):
        
        # Constante que representa o comprimento total de espaços alocados
        # na memória — podendo estar livres (None) ou preenchidos com valores.
        self.__LENGTH = length
        
        # Flag que restringe o array a um único tipo de dado.
        # Define tanto a homogeneidade quanto o modo de operação:
        # tipo escalar → Modo Primitivo | tipo container → Modo Aninhado.
        self.__TYPEARRAY = typecode 
         
        # Tamanho lógico do array — quantidade de espaços efetivamente
        # preenchidos com valores válidos. Sempre <= __LENGTH.
        self._size = 0
        
        # Estrutura interna de armazenamento — ndarray NumPy inicializado
        # com None em todas as posições, representando memória alocada
        # porém ainda não preenchida.
        self.__arrayElements: np.ndarray = np.array([None] * self.__LENGTH)
        
        if values is not None:
            
            # Fluxo 1 — Modo Primitivo (tipos heterogêneos entre values e typecode):
            # O tipo de 'values' difere do typecode — indica que 'values' é um
            # container externo cujos elementos internos serão desempacotados e
            # injetados individualmente no array.
            #
            # Restrição: elementos internos devem ser exclusivamente primitivos.
            # Containers internos violam a homogeneidade do Modo Primitivo e são
            # rejeitados com TypeError.
            #
            # Exemplo válido:
            #   typecode = str(), values = ['a', 'b', 'c']
            #   type(list) ≠ type(str) → Fluxo 1
            #   injeta 'a', 'b', 'c' individualmente → ['a', 'b', 'c', None, None]
            #
            # Exemplo rejeitado:
            #   values = [['a', 'b'], 'c']  → TypeError (lista dentro da lista)
            if type(values) is not type(self.__TYPEARRAY):
                
                # Verifica se algum elemento interno é um container —
                # se sim, rejeita imediatamente para preservar a homogeneidade.
                # O any() para na primeira violação encontrada — O(n) pior caso.
                if any(isinstance(element, (list, np.ndarray, StaticArray)) for element in values):
                    raise TypeError(
                        "Elementos internos não podem ser containers no Modo Primitivo. "
                        "Para aninhamento, defina typecode como list, np.ndarray ou StaticArray."
                    )
                
                match values:
                    
                    # values é uma lista Python nativa —
                    # desempacota e injeta cada elemento escalar
                    # individualmente nas posições alocadas.
                    case list():
                        
                        if len(values) > self.__LENGTH:
                            raise MemoryError("Não é possível inserir todos os dados, pouca memória alocada.")
                        
                        for valueElement in values:
                            self.__arrayElements[self._size] = valueElement
                            self._size += 1
                    
                    # values é um ndarray NumPy —
                    # desempacota e injeta cada elemento preservando
                    # os valores originais do ndarray.
                    case np.ndarray():
                        
                        if len(values) > self.__LENGTH:
                            raise MemoryError("Não é possível inserir todos os dados, pouca memória alocada.")
                        
                        for valueElement in values:
                            self.__arrayElements[self._size] = valueElement
                            self._size += 1
                    
                    # values é outro StaticArray —
                    # desempacota via __iter__ e injeta cada elemento
                    # individualmente, incluindo os None das posições vazias.
                    case StaticArray():    
                        
                        if len(values) > self.__LENGTH:
                            raise MemoryError("Não é possível inserir todos os dados, pouca memória alocada.")
                        
                        for valueElement in values:
                            self.__arrayElements[self._size] = valueElement
                            self._size += 1

            else:
                
                # Fluxo 2 — Modo Aninhado (tipos homogêneos entre values e typecode):
                # O tipo de 'values' é idêntico ao typecode — indica que cada elemento
                # de 'values' é tratado como um elemento individual do array,
                # viabilizando estruturas multidimensionais de tamanho fixo.
                #
                # A validação de MemoryError é omitida pois o Fluxo 2 pressupõe
                # que o typecode já garante compatibilidade estrutural entre
                # o container externo e o array interno.
                #
                # Exemplo válido:
                #   typecode = list(), values = [['a','b'], ['c','d']]
                #   type(list) == type(list) → Fluxo 2
                #   injeta ['a','b'] e ['c','d'] como elementos individuais
                #   output → [['a','b'], ['c','d']]
                
                
                # Verifica se algum elemento interno é um escalar(tipo primitivo) —
                # se sim, rejeita imediatamente para preservar a homogeneidade.
                # O any() para na primeira violação encontrada — O(n) pior caso.
                
                if any(isinstance(element, (str,int,float,bool)) for element in values):
                    raise TypeError(
                        "Elementos internos não podem ser um escalar no Modo Aninhado. "
                    )
                
                match values:
                    
                    # values é uma lista cujo typecode também é list —
                    # cada sublista é um elemento individual do array,
                    # viabilizando arrays de listas (estrutura bidimensional).
                    case list():
                        
                        for valueElement in values:
                            self.__arrayElements[self._size] = valueElement
                            self._size += 1
                    
                    # values é um ndarray cujo typecode também é ndarray —
                    # cada subarray NumPy é um elemento individual do array,
                    # viabilizando arrays de arrays NumPy.
                    case np.ndarray():
                        
                        for valueElement in values:
                            self.__arrayElements[self._size] = valueElement
                            self._size += 1
                    
                    # values é um StaticArray cujo typecode também é StaticArray —
                    # cada elemento do StaticArray externo é um elemento individual,
                    # viabilizando matrizes compostas por instâncias da própria classe.
                    case StaticArray():    
                        
                        for valueElement in values:
                            self.__arrayElements[self._size] = valueElement
                            self._size += 1

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
    #   staticArray._size  → 2  (mesma fonte de verdade)
    #
    # Complexidade:
    #   O(1) — acesso direto ao atributo _size, sem iteração.
    def __len__(self):
        return self._size
    
    # Dunder method que controla a representação do objeto como string.
    # Chamado implicitamente pelo Python quando se usa print() ou str().
    # Sem ele, print(staticArray) exibiria o endereço de memória do objeto.
    # Retorna o ndarray completo — incluindo as posições vazias (None) —
    # permitindo visualizar a estrutura real alocada em memória.
    #
    # Exemplo:
    #   print(staticArray) → ["a" "b" None None None None None None]
    def __str__(self):
        return str(self.__arrayElements)
    
    # Dunder method que torna o objeto iterável.
    # Chamado implicitamente pelo Python em loops for e
    # funções como list(), tuple(), etc.
    # Itera sobre o comprimento total alocado na memória (__LENGTH),
    # incluindo as posições vazias (None).
    #
    # O yield transforma este método em um gerador — ao invés de retornar
    # todos os valores de uma vez, pausa a execução a cada iteração,
    # retorna o valor atual e retoma de onde parou na próxima chamada.
    # Isso evita carregar todos os elementos na memória simultaneamente.
    #
    # Exemplo:
    #   for element in staticArray:
    #       print(element)  ← percorre todos os slots, incluindo None
    def __iter__(self):
        for index in range(self.__LENGTH):
            yield self.__arrayElements[index]

    # Dunder method que permite acesso por índice via colchetes.
    # Chamado implicitamente pelo Python quando se usa array[idx].
    # Respeita o intervalo total alocado [0, LENGTH], incluindo
    # as posições vazias (None).
    #
    # Exemplo:
    #   staticArray[0]  → primeiro elemento alocado
    #   staticArray[9]  → décimo elemento alocado (pode ser None)
    #
    # Raises:
    #   IndexError: Se o índice estiver fora do intervalo alocado [0, LENGTH].
    def __getitem__(self, idx: int):
        if idx < 0 or idx > self.__LENGTH:
            raise IndexError(f'Índice {idx} fora do intervalo válido [0, {self.__LENGTH}].')
        return self.__arrayElements[idx]
        
    def getFirstElement(self):  
        # Retorna o primeiro elemento do array alocado na memória
        # acessando diretamente o índice 0 via __getitem__.
        # Pode retornar None se nenhum valor foi inserido.
        # Complexidade: O(1) — acesso via índice fixo.
        return f"Primeiro elemento: {self[0]}"

    def getLastElement(self):
        # Retorna o último elemento da capacidade alocada do array
        # acessando o índice LENGTH-1 via __getitem__,
        # respeitando o conceito de indexação base zero (n-1).
        #
        # Atenção: retorna a última posição ALOCADA — não o último
        # elemento válido. Para o último válido, utilize _size-1.
        # Complexidade: O(1) — acesso via índice fixo.
        return f"Ultimo elemento do array: {self[self.__LENGTH - 1]}"

    def insertValueElement(self, new_value) -> None:
        """
        Insere um novo elemento na próxima posição disponível do array.

        Acessa diretamente a primeira posição livre através de _size,
        insere o valor e incrementa o tamanho lógico. A inserção sempre
        ocorre no final dos elementos válidos, preservando a ordem de
        inserção dos demais.

        A homogeneidade é garantida pela comparação de tipo entre o valor
        inserido e o typecode definido na instanciação — qualquer tipo
        divergente é rejeitado com TypeError.

        Exemplo:
            antes:  [1, 2, 3, None, None, None]  _size=3
            inserir valor 4:
            depois: [1, 2, 3, 4, None, None]     _size=4

        Complexidade:
            - Tempo:  O(1) — acesso direto via índice _size.
            - Espaço: O(1) — nenhuma estrutura auxiliar criada.

        Args:
            new_value: Valor a ser inserido. Deve ser do mesmo tipo
            definido pelo typecode na instanciação do array.

        Raises:
            MemoryError: Se o array estiver cheio (_size >= LENGTH),
            pois o container não permite redimensionamento.
            TypeError: Se o tipo do valor inserido divergir do typecode,
            violando a homogeneidade do array.
        """
        if self._size > self.__LENGTH:
            raise MemoryError('O ARRAY ESTA COM TODOS OS ESPAÇOS ALOCADOS PREENCHIDOS (CHEIO)!')

        if type(new_value) is type(self.__TYPEARRAY):
            self.__arrayElements[self._size] = new_value
            self._size += 1
        else:
            raise TypeError("Typecode element not equal the typecode Array")
                
    def removeLastElement(self) -> None:
        """
        Remove o último elemento válido do array.

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
        Remove um elemento do array pelo seu índice.

        Utiliza a estratégia de substituição (swap) pelo último elemento válido,
        operando em duas etapas:

            1. O elemento na posição `idx` é sobrescrito pelo último elemento
               válido do array (posição _size-1), preenchendo o buraco gerado
               pela remoção.

            2. A última posição (_size-1), que agora está duplicada, é limpa
               com None e o tamanho lógico é decrementado.

        Exemplo:
            antes:  [1, 2, 3, 4, 5, None, None, None]  _size=5
            remover idx=1 (valor 2):
            passo1: [1, 5, 3, 4, 5, None, None, None]  ← último (5) copiado para idx=1
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
        elif idx < 0 or idx > self._size:
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

        Aplicável apenas em arrays no Modo Primitivo — em arrays aninhados
        a comparação entre containers é semanticamente ambígua.

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
            ValueError: Se o array estiver vazio.
            TypeError:  Se o objeto passado não for uma instância de StaticArray.
        """
        if not isinstance(array, StaticArray):
            raise TypeError("O objeto passado não é uma instância de StaticArray!")

        if len(array) == 0:
            raise ValueError("O array está vazio!")

        max_idx = 0

        for idx in range(array._size):
            if array[idx] > array[max_idx]:
                max_idx = idx

        return max_idx, array[max_idx]
    
    def minElementIntoArray(self, array: object) -> tuple:
        """
        Localiza o menor elemento dentro de um StaticArray e retorna
        seu índice e valor.

        Percorre todos os elementos válidos do array comparando cada um
        com o menor valor encontrado até o momento — estratégia conhecida
        como Linear Search for Minimum. O índice do menor elemento é
        atualizado sempre que um valor inferior ou igual é encontrado.

        Aplicável apenas em arrays no Modo Primitivo — em arrays aninhados
        a comparação entre containers é semanticamente ambígua.

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
            if array[idx] <= array[min_idx]:
                min_idx = idx

        return min_idx, array[min_idx]
    
    def find(self, target) -> np.ndarray | None:
        """
        Busca um elemento no array pelo seu valor e retorna
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
    
    def traverse(self, callback: callable):
        """
        Percorre todos os elementos do array aplicando uma função de callback.

        A operação de travessia (traversal) é uma das operações fundamentais
        em estruturas de dados lineares. Ela consiste em visitar sistematicamente
        cada elemento exatamente uma vez, do índice 0 até LENGTH-1, sem modificar
        a estrutura subjacente.

        Itera sobre o comprimento total alocado (__LENGTH), incluindo as posições
        vazias (None) — permitindo ao callback inspecionar o estado real do container
        em memória, não apenas os elementos válidos.

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
            a travessia. Deve aceitar dois argumentos: o índice atual
            e o valor do elemento na posição correspondente.

        Example:
            >>> sa = StaticArray(5, int())
            >>> sa.insertValueElement(10)
            >>> sa.insertValueElement(20)
            >>> sa.traverse(callback=print)
            0 10
            1 20
            2 None
            3 None
            4 None
        """
        for index, element in enumerate(self.__arrayElements):
            callback(index, element)
    
    # Aqui vamos tornar o nosso array estático e desordenado
    # em um array estático e ordenado — implementação futura
    # de algoritmos como BubbleSort, SelectionSort ou InsertionSort,
    # que viabilizarão a substituição da Busca Linear O(n)
    # pela Busca Binária O(log n) no método find().
    # Aplicável apenas no Modo Primitivo.
    def sortArray(self):
        if isinstance(self.__arrayElements[0], (int, float)):
            n = len(self.__arrayElements)
            # Loop externo para múltiplas passagens
            for i in range(n):
                # Loop interno para comparar pares adjacentes
                for j in range(0, n - i - 1):
                    if self.__arrayElements[j] > self.__arrayElements[j + 1]:
                        # Swap correto usando atribuição múltipla
                        self.__arrayElements[j], self.__arrayElements[j + 1] = self.__arrayElements[j + 1], self.__arrayElements[j]
            return self.__arrayElements
        else: 
            raise ValueError("Não é permitido ordenação de instâncias de elementos que não sejam inteiros ou floats")
            
    
if __name__ == "__main__":
    
    # Array no Modo Aninhado — typecode e values são ambos list.
    # Cada sublista é tratada como um elemento individual do container.
    # Classificado como UnSortedArray pois os elementos
    # serão inseridos sem critério de ordenação.
    staticArray = StaticArray(5, list(), [['a','b','c','d'], ['a','b','d']])

    print(staticArray.getFirstElement())
    print(staticArray.getLastElement())
    
    for i in range(3):
        staticArray.insertValueElement(['1','2','4'])
      
    # removendo tres elementos do array
    for i in range(2):
        staticArray.removeLastElement()
    
    #print(staticArray)  
    
    # iterando sobre o array e printa o valor do elemento
    staticArray.traverse(print)
    
    print(staticArray.removeElementWithIndex(0))
    
    # staticArray.traverse(print)
    
    print(staticArray.find(staticArray[1]))
    
    #print(staticArray)
    #print(len(staticArray))    

    #sys.exit(0)
    
    counters=StaticArray(50,int())
    
    for i in range(49):
        
        if counters._size <= i:
            
            counters.insertValueElement(i+1) 

    print(staticArray.maxElementIntoArray(counters))
    print(staticArray.minElementIntoArray(counters))
    
    counters.insertValueElement(48)
    
    print(counters.sortArray())