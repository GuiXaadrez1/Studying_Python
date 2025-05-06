'''

Crie t1 = (1, 2, 3) e t2 = (4, 5). Gere uma nova tupla t3 que seja a concatenação de
t1 + t2.

Em seguida, multiplique t3 por 2 e explique por que o resultado não altera a imutabilidade
dos elementos originais.

'''

t1 = (1, 2, 3) # tupla 1

print(id(t1)) # 1762245197888

t2 = (4, 5) # tupla 2

print(id(t2)) # 1762243427584

t3 = t1 + t2 # concatenando as tuplas
print(t3)

print(id(t3)) # 1762245095680

print(t3*2) # aqui estamos repetindo os valores da concatenção existente na tupla3

print(id(t3*2)) # 2111724947648

'''
RESPOSTA !

Tupla = estrutura imutável

Não existe operação “in-place” que altere o conteúdo de uma tupla. Qualquer 
“modificação” (concatenação, repetição, slicing etc.) sempre cria uma nova tupla,
deixando as originais totalmente intactas.

Espaços de memória distintos
Cada tupla resultante (t3, depois t3 * 2) é alocada em um endereço de memória diferente.
Seus prints de id(...) comprovam isso.

Reuso de elementos imutáveis
Os valores internos (os inteiros 1, 2, 3, …) são objetos imutáveis também, 
e podem até mesmo ser compartilhados (ter o mesmo id) entre diferentes tuplas. 
Mas a tupla em si nunca muda — seja ela t1, t2, t3 ou o resultado de t3 * 2.

'''