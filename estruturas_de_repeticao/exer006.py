#Contar vogais em uma string com for
# Definir a string
palavra = "liquidificador"

# Inicializar contador
contador_vogais = 0

# Loop para verificar cada letra
for letra in palavra:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:  # Verifica se é vogal (case insensitive)
        contador_vogais += 1

# Imprimir resultado
print(f"Vogais: {contador_vogais}")