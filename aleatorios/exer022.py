#Ler um valor e escrever se é positivo, negativo ou zero (ver o exercício 23).

numero = int(input("Digite um número qualquer: "))

if numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print("O número é ZERO")