#Verificar categoria de produto com elif
preco = float(input("Digite o preço: "))

if preco < 50:
    print("BARATO")
elif preco < 100:
    print("MÉDIO")
else:
    print("CARO")