'''
Dado notas = {'Alice': 9.5, 'Bob': 7.0, 'Carol': 8.3}
use três loops distintos para iterar sobre:

    chaves (for aluno in notas:)

    valores (for nota in notas.values():)

    pares (for aluno, nota in notas.items():)

Para cada aluno, imprima "Alice → 9.5" etc.

'''

notas = {'Alice': 9.5, 'Bob': 7.0, 'Carol': 8.3}

# INTERANDO SOBRE CHAVES
for aluno in notas.keys():
    print('Alice → 9.5')
    
# INTERANDO SOBRE VALORES
for i in notas.values():
    print(i)

# INTERANDO SOBRE ITEMS VULGO PARES DE CHAVE E VALOR
for i in notas.items():
    print(i)
