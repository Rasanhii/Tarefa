num_lados = int(input("Digite o número de lados do polígono regular: "))

if num_lados == 3:
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = (base * altura) / 2
    print("TRIÂNGULO, área =", area)
elif num_lados == 4:
    lado = float(input("Digite o lado do quadrado: "))
    area = lado ** 2
    print("QUADRADO, área =", area)
elif num_lados == 5:
    print("PENTÁGONO")
else:
    print("Número de lados inválido")
