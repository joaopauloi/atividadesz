alunos = {}

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

soma_notas = sum(alunos.values())
media = soma_notas / len(alunos)

print(f"A média das notas dos alunos é: {media:.2f}")




