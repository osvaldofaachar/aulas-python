#Verificar se um ano é bissexto básico com else
ano_bissexto = int(input("Digite um ano: "))

if ano_bissexto % 4 == 0:
    print(f"O ano {ano_bissexto} é bissexto")
else:
    print(f"O ano {ano_bissexto} não é bissexto")