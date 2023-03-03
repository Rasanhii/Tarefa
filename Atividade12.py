alt = float(input("Digite sua altura em metros: "))
se = int(input("Digite seu sexo (1 para feminino e 2 para masculino): "))

if se == 1:
    pe_ide = 62.1 * alt - 44.7
    print("Seu peso ideal é:", pe_ide, "kg")
elif se == 2:
    pe_ide = 72.7 * alt - 58
    print("Seu peso ideal é:", pe_ide, "kg")
else:
    print("Sexo inválido. Digite 1 para feminino ou 2 para masculino.")
