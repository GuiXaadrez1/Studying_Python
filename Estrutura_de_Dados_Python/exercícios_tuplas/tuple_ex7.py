'''

Tuplas Aninhadas e Iteração

Crie uma tupla matriz = ((1,2,3), (4,5,6), (7,8,9)).

Use dois loops for aninhados para imprimir cada elemento no formato 
"linha i, coluna j: valor".

Crie uma lista de todas as diagonais principais (elementos onde linha == coluna).

'''

# Usei o chagot para me ajudar a entender esse cara aqui

# 1) Defina a tupla aninhada
matriz = ((1,2,3), (4,5,6), (7,8,9)) # tupla alinhada

# 2) Percorra com dois for aninhados e imprima cada elemento
for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        print(f"linha {i}, coluna {j}: {valor}")

# 3) Construa a lista das diagonais principais (onde i == j)
diagonais = []
for i, linha in enumerate(matriz):
    # pega elemento onde índice de linha == índice de coluna
    diagonais.append(linha[i])

print("\nDiagonais principais:", diagonais)

'''

Para representar uma matriz 3×3 em Python usando tuplas, definimos:

    matriz = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
    )

    Cada elemento de matriz é uma linha, que por sua vez é uma tupla de colunas.

Iteração aninhada com enumerate

    Usamos enumerate(matriz) para obter, em cada iteração do laço externo, dois valores:

    i: o índice da linha (0 para a primeira, 1 para a segunda, 2 para a terceira).

    linha: a tupla que contém os elementos dessa linha.

    Dentro desse laço, fazemos outro for com enumerate(linha), o que nos dá:

    j: o índice da coluna dentro da linha atual.

    valor: o número armazenado naquela posição.

Em cada passagem do laço interno, imprimimos uma mensagem no formato:

    linha i, coluna j: valor

    Assim, “linha 1, coluna 2: 6” significa que, na segunda linha (índice 1) e 
    terceira coluna (índice 2), o valor é 6.

Construção da lista de diagonais principais

    A diagonal principal de uma matriz são os elementos cuja linha e coluna têm o mesmo
    índice (i == j).

    Como já temos i no laço externo, basta extrair o elemento linha[i] para cada linha.

    Podemos, portanto, iniciar uma lista vazia diagonais = [] e, a cada iteração do
    laço externo, fazer diagonais.append(linha[i]).

    No nosso exemplo, isso acrescenta os valores 1 (linha 0, coluna 0), 
    5 (linha 1, coluna 1) e 9 (linha 2, coluna 2), resultando em [1, 5, 9].

    Por que isso funciona?

    Usar enumerate em tuplas é tão eficiente quanto em listas, pois tuplas também 
    suportam indexação e iteração.

    A abordagem por “linha externa” e “coluna interna” replica exatamente a lógica de
    percorrer uma matriz tradicional.

    Extrair a diagonal principal tirando linha[i] evita testes condicionais adicionais
    dentro do laço interno, simplificando o código e mantendo a clareza.

Resumo do fluxo

    Linha 1: i = 0, percorre valores (1,2,3) com j = 0,1,2. Imprime “linha 0, coluna 0: 1”,
    “linha 0, coluna 1: 2” etc. Depois adiciona linha[0] (1) à lista de diagonais.

    Linha 2: i = 1, percorre (4,5,6), imprime “linha 1, coluna 0: 4” etc., 
    adiciona linha[1] (5).

    Linha 3: i = 2, percorre (7,8,9), imprime “linha 2, coluna 0: 7” etc., 
    adiciona linha[2] (9).

    Ao final, diagonais == [1, 5, 9].

'''