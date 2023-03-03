a1 = float(input("Digite o valor inicial da PG: "))
n = int(input("Digite a quantidade de termos da PG: "))
q = float(input("Digite a razão da PG (deve ser maior ou igual a 2): "))

if q < 2:
    print("A razão deve ser maior ou igual a 2.")
else:
    som = a1 * (q**n - 1) / (q-1)
    print(f"A soma é {som}.")
