# Aqui vamos entender como se comporta a instância da nossa class StaticArray

from Estrutura_Dados.array.static.StaticArray import StaticArray

memoryBuffer = StaticArray(20,float,[10.5,20,30,40,50,44,12,16,17,8,90,1,2,3,4,5,6,7,8,100])

# print(memoryBuffer.maxElementIntoArray(memoryBuffer),memoryBuffer.minElementIntoArray(memoryBuffer))

print(memoryBuffer.sortNumericArrayStatic())