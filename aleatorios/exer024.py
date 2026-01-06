#Ler três valores  e escrever a soma dos dois maiores.

# Leitura dos três valores
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

# Estrutura condicional para encontrar o menor e somar os outros dois
if a <= b and a <= c:
    # a é o menor, soma b + c
    soma = b + c
elif b <= a and b <= c:
    # b é o menor, soma a + c
    soma = a + c
else:
    # c é o menor, soma a + b
    soma = a + b

# Exibir o resultado
print("A soma dos dois maiores valores é:", soma)
