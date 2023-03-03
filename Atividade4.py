nome_aluno = input("Digite o nome do aluno: ")
nota_aluno = float(input("Digite a nota do aluno: "))

print("ALUNO(A)            NOTA")
print("=========         =====")
print(f"{nome_aluno.ljust(18)}{nota_aluno}")
