#Ler três valores (considere que não serão informados valores iguais) e escrever o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O Primeiro Número é o Maior")
elif num2 > num1 and num2 > num3:
    print("O Segundo Número é o Maior")
else:
    print("O Terceiro Número é o Maior")