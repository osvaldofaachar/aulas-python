valores = input("Digite 3 números separados por espaço: ")
n1, n2, n3 = valores.split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

media = (n1 + n2 + n3) / 3

print(f"A média é {media}")
