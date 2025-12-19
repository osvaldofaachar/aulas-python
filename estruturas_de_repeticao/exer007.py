#Tabuada Simples com Loops Aninhados

# Loop externo para os números da tabuada (1 a 3)
for i in range(1, 4):
    # Loop interno para multiplicar por 1 a 3
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}")
    print()  # Linha em branco para separar cada tabuada