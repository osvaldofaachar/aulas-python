#Verificar faixa etária com elif

idade = int(input("Digite a sua idade: "))

if idade < 13:
    print("CRIANÇA")
elif idade < 18:
    print("ADOLESCENTE")
else:
    print("ADULTO")