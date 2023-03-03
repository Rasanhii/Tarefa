n_lados = int(input("Digite o número de lados do polígono regular: "))

if n_lados < 3:
    print("Não é um polígono")
elif n_lados == 3:
    base = float(input("Digite a medida da base do triângulo: "))
    altura = float(input("Digite a medida da altura do triângulo: "))
    area = (base * altura) / 2
    print(f"TRIÂNGULO - Área: {area}")
elif n_lados == 4:
    lado = float(input("Digite a medida do lado do quadrado: "))
    area = lado ** 2
    print(f"QUADRADO - Área: {area}")
elif n_lados == 5:
    print("PENTÁGONO")
else:
    print("[Erro]")
