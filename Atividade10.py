ano = 2023
ano_nas = int(input("Digite o ano de nascimento: "))
ida = ano - ano_nas

if ida >= 18:
    print("Você pode votar este ano!")
else:
    print("Desculpe, você ainda não pode votar este ano.")
