# Aqui vamos entender como se comporta a instância da nossa class StaticArray

import time # sempre importe os pacotes que inicia com import primeiro depois os from
import random as rd
import sys

from Estrutura_Dados.array.static.StaticArray import StaticArray

memoryBuffer = StaticArray(50,int(),[10,20,30,40,50,44,12,16,17,8,90,1,2,3,4,5,6,7,8,100])

start_time = time.time()

for i in range(0,20):
    
    num:int = rd.randint(0,3000)
    
    memoryBuffer.insertValueElement(num)
    
print(memoryBuffer.sortNumericStaticArray())

print(memoryBuffer.maxElementIntoArray(memoryBuffer),memoryBuffer.minElementIntoArray(memoryBuffer))

print(memoryBuffer.insertIntoSortArray(0))

end_time = time.time()

print(f'tempo de execução: {end_time - start_time:.2f}')


