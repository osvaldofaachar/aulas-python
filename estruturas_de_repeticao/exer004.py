#Encontrar um número em uma lista com break

lista = [10, 20, 30, 40]
numero = int(input("Escolha um número: "))

for num in lista:
    if numero == num:
        print("Encontrado!", num)
        break
