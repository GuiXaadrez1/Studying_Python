'''

Teste "Alice" in notas e "Dave" in notas.

Crie um novo dict aprovados contendo apenas alunos com nota ≥ 8.0, usando um loop 
ou comprehension.

'''

notas = {'Alice': 9.5, 'Bob': 7.0, 'Carol': 8.3}

print("Alice" in notas) # True
print("Dave" in notas) # False


# Usando o for loops

aprovados = {}
for aluno,valor in notas.items():
    if valor >= 8.0:
        aprovados.update({aluno:valor})

for aluno, valor in aprovados.items():
    print(f'Aluno: {aluno} | Nota: {valor} | Status: Aprovado')   
   