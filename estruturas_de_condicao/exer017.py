#Verificar elegibilidade para empréstimo com and

idade = int(input("Digite a sua idade: "))
renda = float(input("Digite a sua renda: "))

if idade >= 21 and renda >= 2000:
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")