#Jogo de Soma com while e break Complexo

# Loop infinito até break
while True:
    # Pedir dois números
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # Calcular soma
    soma = num1 + num2
    print(f"Soma: {soma}")

    # Verificar se soma é 10 e parar
    if soma == 10:
        print("Fim!")
        break