# Quero que faça operações aritíméticas entre duas listas
# primiera lista com tamanhos iguas 
# segunda lista com tamanhos diferentes 

import numpy as np

lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30]

# Determinar o tamanho máximo
max_len = max(len(lista1), len(lista2))

# Preencher as listas com 0 até terem o mesmo tamanho
pad_lista1 = lista1 + [0] * (max_len - len(lista1))
pad_lista2 = lista2 + [0] * (max_len - len(lista2))

# Converter para arrays NumPy
array1 = np.array(pad_lista1)
array2 = np.array(pad_lista2)

soma = array1 + array2
print(soma)# Saída: [11 22 33 4]

total = sum(soma)
print(total)# 70