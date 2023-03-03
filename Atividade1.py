n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
me = float(input("Digite a média dos exercícios: "))

ma = (n1 + n2*2 + n3*3 + me)/7

if ma >= 9:
    print("Maior ou igual a 9")
elif ma <= 4:
    print("Menor ou igual a 4")
else:
    print("Na média")
