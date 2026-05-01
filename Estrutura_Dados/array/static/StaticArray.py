import numpy as np
import sys

class StaticArray:
    
    """
    Container de tamanho fixo com suporte a tipagem homogênea e aninhamento.

    Simula o comportamento de um Array Estático inspirado no conceito de vetores
    unidimensionais homogêneos de linguagens como C — onde o tipo de dado é definido
    na instanciação e não pode ser alterado. O tamanho é fixo e não permite
    redimensionamento após a criação.

    Nota conceitual:
        Quando se trabalha com estruturas estáticas, operamos sobre vetores —
        regiões contíguas de memória de tamanho fixo acessadas por índice.
        Quando se trabalha com estruturas dinâmicas, operamos sobre ponteiros —
        referências a regiões de memória que podem ser realocadas em tempo de execução.
        Esta implementação simula o comportamento estático usando NumPy como
        substrato de alocação contígua.

    Suporta dois modos de operação mutuamente exclusivos, determinados pelo typecode:

        Modo Primitivo (Fluxo 1):
            O typecode define um tipo escalar (str, int, float, bool).
            Os valores injetados via `values` devem ser exclusivamente escalares —
            containers internos são rejeitados para preservar a homogeneidade.
            Destinado a vetores unidimensionais de elementos primitivos,
            equivalente a int arr[n] ou float arr[n] em C.

            Exemplo válido:
                StaticArray(5, str(), ['a', 'b', 'c'])
                output → ['a', 'b', 'c', None, None]

            Exemplo rejeitado:
                StaticArray(5, str(), [['a', 'b'], 'c'])
                → TypeError: containers internos não são permitidos no Modo Primitivo.

        Modo Aninhado (Fluxo 2):
            O typecode define um container (list, np.ndarray, StaticArray).
            Os valores injetados via `values` devem ser exclusivamente containers —
            escalares internos são rejeitados para preservar a homogeneidade estrutural.
            Destinado a estruturas multidimensionais de tamanho fixo,
            onde cada elemento do array é ele mesmo um container,
            simulando o comportamento de uma matriz estática (int matrix[m][n] em C).

            Exemplo válido:
                StaticArray(2, list(), [['a', 'b'], ['c', 'd']])
                output → [['a', 'b'], ['c', 'd']]

            Exemplo rejeitado:
                StaticArray(2, list(), [['a', 'b'], 'c'])
                → TypeError: escalares internos não são permitidos no Modo Aninhado.

    Características:

        - Tamanho fixo definido na instanciação — não permite redimensionamento.
        - Tipagem homogênea — aceita apenas um tipo de dado por instância.
        - Indexação baseada em zero (0 até length - 1).
        - Acesso a qualquer elemento em tempo constante O(1).
        - Suporta estruturas unidimensionais (Modo Primitivo) e
          multidimensionais de tamanho fixo (Modo Aninhado).
        - Iterável via protocolo Python (__iter__, __getitem__).
        - Ordenação numérica via BubbleSort — exclusiva do Modo Primitivo
          com typecode int ou float.

    Args:
        length   (int): Quantidade de posições a reservar na memória.
                 Define o tamanho físico imutável do container.
        typecode (str | int | float | bool | list | np.ndarray | object):
                 Tipo de dado aceito pelo array. Define a homogeneidade
                 e o modo de operação:
                 - Escalar (str, int, float, bool) → Modo Primitivo
                 - Container (list, np.ndarray, StaticArray) → Modo Aninhado
        values   (list | np.ndarray | StaticArray | None): Valores iniciais
                 opcionais a serem injetados na instanciação.
                 - Modo Primitivo: apenas escalares são permitidos internamente.
                 - Modo Aninhado: apenas containers são permitidos internamente.
                 Padrão: None — array inicializado vazio.

    Raises:
        MemoryError: Se o número de valores em `values` exceder o `length` alocado.
        TypeError:   Se no Modo Primitivo algum elemento interno for um container,
                     ou se no Modo Aninhado algum elemento interno for um escalar.
        ValueError:  Se no Modo Primitivo algum elemento interno divergir do typecode
                     definido, violando a homogeneidade do array.

    Example:

        >>> # Modo Primitivo — vetor unidimensional homogêneo
        >>> sa = StaticArray(5, str(), ['a', 'b', 'c'])
        >>> print(sa)
        ['a' 'b' 'c' None None]

        >>> # Modo Aninhado — matriz estática de tamanho fixo
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
        # Equivalente ao tamanho declarado em int arr[LENGTH] em C.
        self.__LENGTH = length
        
        # Flag que restringe o array a um único tipo de dado.
        # Define tanto a homogeneidade quanto o modo de operação:
        # tipo escalar → Modo Primitivo | tipo container → Modo Aninhado.
        self.__TYPEARRAY = typecode 
         
        # Tamanho lógico do array — quantidade de espaços efetivamente
        # preenchidos com valores válidos. Sempre <= __LENGTH.
        # Distinção fundamental: __LENGTH é o tamanho físico (alocado),
        # _size é o tamanho lógico (preenchido).
        self._size = 0
        
        # Estrutura interna de armazenamento — ndarray NumPy inicializado
        # com None em todas as posições, representando memória alocada
        # porém ainda não preenchida (equivalente a lixo de memória em C,
        # aqui substituído por None para segurança em Python).
        self.__arrayElements: np.ndarray = np.array([None] * self.__LENGTH)
        
        if values is not None:
            
            # Fluxo 1 — Modo Primitivo (tipos heterogêneos entre values e typecode):
            # O tipo de 'values' difere do typecode — indica que 'values' é um
            # container externo cujos elementos internos serão desempacotados e
            # injetados individualmente no array.
            #
            # Restrições:
            #   1. Elementos internos devem ser exclusivamente escalares primitivos.
            #   2. Cada elemento deve ser do mesmo tipo que o typecode definido —
            #      garantindo homogeneidade estrita elemento a elemento.
            #
            # Exemplo válido:
            #   typecode = str(), values = ['a', 'b', 'c']
            #   type(list) ≠ type(str) → Fluxo 1
            #   injeta 'a', 'b', 'c' individualmente → ['a', 'b', 'c', None, None]
            #
            # Exemplo rejeitado (container interno):
            #   values = [['a', 'b'], 'c'] → TypeError
            #
            # Exemplo rejeitado (tipo divergente):
            #   typecode = str(), values = ['a', 1, 'c'] → ValueError no elemento 1
            if type(values) is not type(self.__TYPEARRAY):
                
                # Guarda de tipo estrutural — rejeita containers internos antes
                # de iniciar a injeção, evitando estado parcialmente preenchido.
                # O any() opera em curto-circuito: para na primeira violação — O(n) pior caso.
                if any(isinstance(element, (list, np.ndarray, StaticArray)) for element in values):
                    raise TypeError(
                        "Elementos internos não podem ser containers no Modo Primitivo. "
                        "Para aninhamento, defina typecode como list, np.ndarray ou StaticArray."
                    )
                
                match values:
                    
                    # values é uma lista Python nativa —
                    # desempacota e injeta cada elemento escalar individualmente,
                    # validando o typecode elemento a elemento antes de cada inserção.
                    case list():
                        
                        if len(values) > self.__LENGTH:
                            raise MemoryError("Não é possível inserir todos os dados, pouca memória alocada.")
                        
                        for _, valueElement in enumerate(values):
                            
                            if type(valueElement) != type(self.__TYPEARRAY):
                                raise ValueError(
                                    f"Array não homogêneo\n"
                                    f"typecode do array: {self.__TYPEARRAY}\n"
                                    f"typecode elemento: {type(valueElement)}\n"
                                    f"index elemento: {self._size}\n"
                                    f"valor elemento: {valueElement}"
                                )
                                                
                            self.__arrayElements[self._size] = valueElement
                            self._size += 1
                    
                    # values é um ndarray NumPy —
                    # desempacota e injeta cada elemento preservando os valores
                    # originais do ndarray, validando homogeneidade elemento a elemento.
                    case np.ndarray():
                        
                        if len(values) > self.__LENGTH:
                            raise MemoryError("Não é possível inserir todos os dados, pouca memória alocada.")
                        
                        for _, valueElement in enumerate(values):

                            if type(valueElement) != type(self.__TYPEARRAY):
                                raise ValueError(
                                    f"Array não homogêneo\n"
                                    f"typecode do array: {self.__TYPEARRAY}\n"
                                    f"typecode elemento: {type(valueElement)}\n"
                                    f"index elemento: {self._size}\n"
                                    f"valor elemento: {valueElement}"
                                )
                                    
                            self.__arrayElements[self._size] = valueElement
                            self._size += 1
                    
                    # values é outro StaticArray —
                    # desempacota via __iter__ e injeta cada elemento individualmente,
                    # validando homogeneidade elemento a elemento.
                    # Atenção: __iter__ percorre __LENGTH — inclui posições None.
                    case StaticArray():    
                        
                        if len(values) > self.__LENGTH:
                            raise MemoryError("Não é possível inserir todos os dados, pouca memória alocada.")
                        
                        for _, valueElement in enumerate(values):
                                                    
                            if type(valueElement) != type(self.__TYPEARRAY):
                                raise ValueError(
                                    f"Array não homogêneo\n"
                                    f"typecode do array: {self.__TYPEARRAY}\n"
                                    f"typecode elemento: {type(valueElement)}\n"
                                    f"index elemento: {self._size}\n"
                                    f"valor elemento: {valueElement}"
                                )
                                                
                            self.__arrayElements[self._size] = valueElement
                            self._size += 1

            else:
                
                # Fluxo 2 — Modo Aninhado (tipos homogêneos entre values e typecode):
                # O tipo de 'values' é idêntico ao typecode — indica que cada elemento
                # de 'values' é tratado como um elemento individual do array,
                # viabilizando estruturas multidimensionais de tamanho fixo.
                #
                # Restrição: elementos internos devem ser exclusivamente containers.
                # Escalares violam a semântica do Modo Aninhado — onde cada posição
                # do array deve conter uma estrutura completa, não um valor primitivo.
                #
                # Exemplo válido:
                #   typecode = list(), values = [['a','b'], ['c','d']]
                #   type(list) == type(list) → Fluxo 2
                #   injeta ['a','b'] e ['c','d'] como elementos individuais
                #   output → [['a','b'], ['c','d']]
                #
                # Exemplo rejeitado:
                #   values = [['a','b'], 'c'] → TypeError (escalar 'c' viola homogeneidade)
                
                # Guarda de tipo escalar — rejeita primitivos internos antes
                # de iniciar a injeção. O any() opera em curto-circuito — O(n) pior caso.
                if any(isinstance(element, (str, int, float, bool)) for element in values):
                    raise TypeError(
                        "Elementos internos não podem ser escalares no Modo Aninhado. "
                        "Para vetores primitivos, defina typecode como str, int, float ou bool."
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
                    # viabilizando arrays de arrays NumPy (equivalente a matriz C).
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
    # Retorna o tamanho lógico (_size) — quantidade de elementos válidos —
    # e não o tamanho físico (__LENGTH). Essa distinção é fundamental:
    # len() deve refletir o que existe no container, não o que foi alocado.
    #
    # Exemplo:
    #   capacidade física:  ["a", "b", None, None, None, None, None, None]  __LENGTH=8
    #   len(staticArray)    → 2  (tamanho lógico) ✅
    #   staticArray._size   → 2  (mesma fonte de verdade)
    #
    # Complexidade: O(1) — acesso direto ao atributo _size, sem iteração.
    def __len__(self):
        return self._size
    
    # Dunder method que controla a representação textual do objeto.
    # Chamado implicitamente pelo Python quando se usa print() ou str().
    # Sem ele, print(staticArray) exibiria o endereço de memória do objeto
    # (ex: <__main__.StaticArray object at 0x...>).
    #
    # Retorna o ndarray completo — incluindo posições vazias (None) —
    # expondo o estado real da memória alocada, não apenas os elementos válidos.
    # Útil para depuração e inspeção da estrutura interna.
    #
    # Exemplo:
    #   print(staticArray) → ["a" "b" None None None None None None]
    def __str__(self):
        return str(self.__arrayElements)
    
    # Dunder method que implementa o protocolo iterável do Python.
    # Chamado implicitamente em loops for, list(), tuple(), enumerate(), etc.
    # Itera sobre o comprimento físico total (__LENGTH), incluindo None —
    # expondo o estado completo da memória alocada ao iterador.
    #
    # Implementado como gerador via yield — ao invés de retornar todos os
    # valores de uma vez (O(n) memória), pausa a execução a cada iteração,
    # retorna o valor atual e retoma de onde parou na próxima chamada.
    # Isso garante consumo de memória O(1) independente do tamanho do array.
    #
    # Exemplo:
    #   for element in staticArray:
    #       print(element)  ← percorre todos os slots, incluindo None
    def __iter__(self):
        for index in range(self.__LENGTH):
            yield self.__arrayElements[index]

    # Dunder method que implementa o protocolo de acesso por índice.
    # Chamado implicitamente pelo Python quando se usa array[idx].
    # Permite acesso a qualquer posição dentro do intervalo físico alocado
    # [0, LENGTH], incluindo posições vazias (None).
    #
    # Complexidade: O(1) — acesso direto por índice, sem iteração.
    #
    # Exemplo:
    #   staticArray[0]  → primeiro elemento alocado
    #   staticArray[9]  → décimo elemento alocado (pode ser None)
    #
    # Raises:
    #   IndexError: Se o índice estiver fora do intervalo físico [0, LENGTH].
    def __getitem__(self, idx: int):
        if idx < 0 or idx > self.__LENGTH:
            raise IndexError(f'Índice {idx} fora do intervalo válido [0, {self.__LENGTH}].')
        return self.__arrayElements[idx]
        
    def getFirstElement(self):  
        # Retorna o primeiro elemento do array acessando o índice 0 via __getitem__.
        # Pode retornar None se nenhum valor foi inserido ainda.
        # Equivalente a arr[0] em C — acesso direto sem percorrer elementos.
        # Complexidade: O(1).
        return f"Primeiro elemento: {self[0]}"

    def getLastElement(self):
        # Retorna o último elemento da capacidade física alocada,
        # acessando o índice __LENGTH-1 via __getitem__.
        # Respeita a indexação base zero: o último índice válido é sempre n-1.
        #
        # Atenção: retorna a última posição FÍSICA (alocada) — que pode ser None.
        # Para o último elemento lógico (válido), utilize self[_size-1].
        # Complexidade: O(1).
        return f"Ultimo elemento do array: {self[self.__LENGTH - 1]}"

    def insertValueElement(self, new_value) -> None:
        """
        Insere um novo elemento na próxima posição disponível do array.

        Acessa diretamente a primeira posição livre através de _size —
        o tamanho lógico atua como ponteiro implícito para a próxima
        posição disponível. A inserção sempre ocorre no final dos elementos
        válidos, preservando a ordem de inserção dos demais.

        A homogeneidade é garantida pela comparação estrita de tipo (type() is)
        entre o valor inserido e o typecode definido na instanciação —
        qualquer divergência de tipo é rejeitada com TypeError.

        Exemplo:
            antes:  [1, 2, 3, None, None, None]  _size=3
            inserir valor 4:
            depois: [1, 2, 3, 4, None, None]     _size=4

        Complexidade:
            - Tempo:  O(1) — acesso direto via índice _size (ponteiro lógico).
            - Espaço: O(1) — nenhuma estrutura auxiliar criada.

        Args:
            new_value: Valor a ser inserido. Deve ser do mesmo tipo
            definido pelo typecode na instanciação do array.

        Raises:
            MemoryError: Se o array estiver cheio (_size >= LENGTH) —
            arrays estáticos têm capacidade física imutável.
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

        Acessa diretamente a última posição ocupada através de _size-1 —
        o tamanho lógico decrementado atua como ponteiro para o último
        elemento válido. Substitui o valor por None e decrementa _size.
        Não há deslocamento de elementos — apenas a última posição é limpa,
        preservando a ordem e posição de todos os demais.

        Exemplo:
            antes:  [1, 2, 3, 4, 5, None, None, None]  _size=5
            depois: [1, 2, 3, 4, None, None, None, None]  _size=4

        Complexidade:
            - Tempo:  O(1) — acesso direto via índice _size-1.
            - Espaço: O(1) — nenhuma estrutura auxiliar criada.

        Raises:
            ValueError: Se o array estiver vazio (_size == 0) —
            não há elemento lógico válido para remover.
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
               pela remoção sem deslocar os demais elementos.

            2. A última posição (_size-1), agora duplicada, é limpa com None
               e o tamanho lógico é decrementado.

        Esta estratégia é eficiente para arrays desordenados (UnSortedArray) —
        opera em O(1) ao custo de não preservar a ordem de inserção.
        Para arrays onde a ordem importa, utilize a estratégia de Shift (O(n)).

        Exemplo:
            antes:  [1, 2, 3, 4, 5, None, None, None]  _size=5
            remover idx=1 (valor 2):
            passo1: [1, 5, 3, 4, 5, None, None, None]  ← último (5) copiado para idx=1
            passo2: [1, 5, 3, 4, None, None, None, None]  _size=4  ← duplicata limpa

        Consequências:
            - O valor removido é destruído (sobrescrito).
            - O último elemento válido muda de posição.
            - A ordem original de inserção não é preservada.
            - O array retorna desordenado em relação à inserção original.

        Complexidade:
            - Tempo:  O(1) — duas atribuições diretas por índice, sem laço.
            - Espaço: O(1) — nenhuma estrutura auxiliar criada.

        Args:
            idx (int): Índice do elemento a ser removido. Deve estar
            no intervalo lógico válido [0, size-1].

        Returns:
            np.ndarray: O array interno atualizado após a remoção.

        Raises:
            ValueError: Se o array estiver vazio (_size == 0).
            ValueError: Se o índice estiver fora do intervalo lógico [0, size-1].
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
        Localiza o maior elemento dentro de um StaticArray pelo seu valor e índice.

        Percorre todos os elementos válidos comparando cada um com o maior valor
        encontrado até o momento — estratégia conhecida como Linear Search for Maximum.
        O índice de referência é atualizado sempre que um valor estritamente superior
        é encontrado, garantindo que em caso de empate o primeiro índice prevalece.

        Aplicável apenas a arrays no Modo Primitivo com typecode numérico (int, float)
        ou lexicográfico (str). Em arrays no Modo Aninhado, a comparação entre
        containers é semanticamente ambígua e pode produzir resultados incorretos.

        Exemplo:
            array: [3, 7, 1, 9, 2, None, None, None]  _size=5
            percorre → 3, 7, 1, 9, 2
            maior encontrado → índice=3, valor=9
            retorna → (3, 9)

        Complexidade:
            - Tempo:  O(n) — todos os elementos válidos são visitados exatamente uma vez.
            - Espaço: O(1) — apenas o índice de referência é mantido em memória.

        Args:
            array (StaticArray): Instância de StaticArray sobre a qual
            a busca pelo maior elemento será realizada.

        Returns:
            tuple: Par (índice, valor) correspondente ao maior elemento
            encontrado no array, onde índice é a primeira ocorrência.

        Raises:
            ValueError: Se o array estiver vazio (_size == 0).
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
        Localiza o menor elemento dentro de um StaticArray pelo seu valor e índice.

        Percorre todos os elementos válidos comparando cada um com o menor valor
        encontrado até o momento — estratégia conhecida como Linear Search for Minimum.
        O índice de referência é atualizado sempre que um valor inferior ou igual
        é encontrado, garantindo que em caso de empate o último índice prevalece.

        Aplicável apenas a arrays no Modo Primitivo com typecode numérico (int, float)
        ou lexicográfico (str). Em arrays no Modo Aninhado, a comparação entre
        containers é semanticamente ambígua e pode produzir resultados incorretos.

        Exemplo:
            array: [3, 7, 1, 9, 2, None, None, None]  _size=5
            percorre → 3, 7, 1, 9, 2
            menor encontrado → índice=2, valor=1
            retorna → (2, 1)

        Complexidade:
            - Tempo:  O(n) — todos os elementos válidos são visitados exatamente uma vez.
            - Espaço: O(1) — apenas o índice de referência é mantido em memória.

        Args:
            array (StaticArray): Instância de StaticArray sobre a qual
            a busca pelo menor elemento será realizada.

        Returns:
            tuple: Par (índice, valor) correspondente ao menor elemento
            encontrado no array, onde índice é a última ocorrência em empate.

        Raises:
            ValueError: Se o array estiver vazio (_size == 0).
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
        Busca um elemento no array pelo seu valor e retorna a primeira ocorrência.

        Por se tratar de um array desordenado (UnSortedArray), não é possível
        aplicar algoritmos de busca eficientes como a Busca Binária — que exige
        ordenação prévia e opera em O(log n). Portanto, utiliza-se a Busca Linear
        (Linear Search): cada elemento é visitado sequencialmente do índice 0
        até _size-1 até que a primeira ocorrência do alvo seja encontrada.

        Após a ordenação via sortNumericStaticArray(), recomenda-se substituir
        esta busca por uma implementação de Busca Binária para ganho de performance.

        Exemplo:
            array: ["a", "b", "c", "d", "e", None, None]  _size=5
            find("c") → percorre índices 0, 1, 2 → encontra "c" → retorna np.array(["c"])
            find("z") → percorre todos os índices → não encontra  → retorna None

        Complexidade:
            - Melhor caso:  O(1) — alvo encontrado no índice 0.
            - Pior caso:    O(n) — alvo no último índice ou inexistente no array.
            - Espaço:       O(1) — nenhuma estrutura auxiliar criada.

        Args:
            target: Valor a ser localizado no array. Deve ser do mesmo
            tipo definido pelo typecode na instanciação.

        Returns:
            np.ndarray contendo a primeira ocorrência encontrada, ou None caso
            o alvo não exista entre os elementos válidos do array.
        """
        for index in range(self._size):
            if self.__arrayElements[index] == target:
                return np.array([self.__arrayElements[index]])

        return None
    
    def traverse(self, callback: callable) -> None:
        """
        Percorre todos os elementos do array aplicando uma função de callback.

        A operação de travessia (traversal) é uma das operações fundamentais
        em estruturas de dados lineares — consiste em visitar sistematicamente
        cada elemento exatamente uma vez, do índice 0 até LENGTH-1, sem modificar
        a estrutura subjacente.

        Itera sobre o comprimento físico total (__LENGTH), incluindo posições
        vazias (None) — expondo ao callback o estado real da memória alocada,
        não apenas os elementos lógicos válidos.

        O parâmetro `callback` segue o padrão de projeto Higher-Order Function —
        uma função que recebe outra função como argumento, desacoplando a lógica
        de iteração da lógica de processamento. Isso torna o método reutilizável
        para qualquer operação: impressão, transformação, filtragem, acumulação, etc.

        Complexidade:
            - Tempo:  O(n) — cada elemento é visitado exatamente uma vez.
            - Espaço: O(1) — nenhuma estrutura auxiliar criada.

        Args:
            callback (callable): Função de ordem superior aplicada a cada elemento
            durante a travessia. Deve aceitar dois argumentos posicionais:
            o índice físico atual (int) e o valor do elemento na posição correspondente.

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
    
    def sortNumericStaticArray(self) -> 'StaticArray':
        """
        Ordena in-place os elementos numéricos válidos do array em ordem crescente.

        Implementa o algoritmo Bubble Sort — um dos algoritmos de ordenação mais
        didáticos da Ciência da Computação. Opera comparando pares adjacentes e
        trocando-os quando estão fora de ordem, repetindo o processo até que
        nenhuma troca seja necessária. A cada passagem completa, o maior elemento
        ainda não ordenado "borbulha" para sua posição correta no final do array.

        A troca de elementos utiliza atribuição múltipla com tuplas do Python —
        uma operação atômica que elimina a necessidade de variável temporária,
        diferente da abordagem clássica em C que requer três atribuições.

        Aplicável exclusivamente ao Modo Primitivo com typecode numérico
        (int ou float). Strings e containers não possuem semântica de ordenação
        numérica e são rejeitados com ValueError.

        Após a ordenação, o método find() pode ser substituído por uma
        implementação de Busca Binária O(log n) para ganho de performance.

        Exemplo:
            antes:  [3, 7, 1, 9, 2, None, None, None]  _size=5
            passo1: [3, 1, 7, 2, 9, None, None, None]  ← 9 borbulhou
            passo2: [1, 3, 2, 7, None, None, None, None] ← 7 borbulhou
            ...
            depois: [1, 2, 3, 7, 9, None, None, None]  ← ordenado ✅

        Complexidade:
            - Melhor caso:  O(n)   — array já ordenado (sem trocas).
            - Caso médio:   O(n²)  — comparações e trocas parciais.
            - Pior caso:    O(n²)  — array em ordem inversa.
            - Espaço:       O(1)   — ordenação in-place, sem estrutura auxiliar.

        Returns:
            StaticArray: Retorna self após a ordenação, permitindo encadeamento
            de chamadas (method chaining).

        Raises:
            ValueError: Se o typecode do array não for int ou float —
            ordenação numérica não é definida para outros tipos.
        """
        if isinstance(self[0], (int, float)):
            
            for i in range(self._size):
                
                for j in range(0, self._size - i - 1):
                    
                    if self[j] > self[j + 1]:
                        
                        # Swap via atribuição múltipla com tuplas —
                        # Python avalia o lado direito completamente antes
                        # de atribuir, eliminando a necessidade de variável
                        # temporária (diferente do swap clássico em C).
                        self.__arrayElements[j], self.__arrayElements[j + 1] = self[j + 1], self[j]
            
            return self
        
        else: 
            raise ValueError(
                "Ordenação numérica aplicável apenas a arrays com typecode int ou float. "
                "Strings e containers não possuem semântica de ordenação numérica."
            )            
    
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
    
    print(staticArray)
    print(len(staticArray))    
    
    counters=StaticArray(50,int())
    
    for i in range(49):
        
        if counters._size <= i:
            
            counters.insertValueElement(i+1) 

    print(staticArray.maxElementIntoArray(counters))
    print(staticArray.minElementIntoArray(counters))
    
    counters.insertValueElement(48)
    
    print(counters.sortNumericStaticArray())