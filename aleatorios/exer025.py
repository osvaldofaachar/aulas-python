# Leitura dos três valores
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

# Estrutura condicional para ordenar e imprimir em ordem crescente
if a < b and a < c:
    if b < c:
        print("Ordem crescente:", a, b, c)
    else:
        print("Ordem crescente:", a, c, b)
elif b < a and b < c:
    if a < c:
        print("Ordem crescente:", b, a, c)
    else:
        print("Ordem crescente:", b, c, a)
else:
    if a < b:
        print("Ordem crescente:", c, a, b)
    else:
        print("Ordem crescente:", c, b, a)