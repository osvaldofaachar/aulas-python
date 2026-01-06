# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e
#quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média, usando a
#seguinte fórmula: ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade
#em estoque for maior ou igual a quantidade média escrever a mensagem “Não efetuar compra”, senão
#escrever a mensagem “Efetuar compra”.

qtd_actual = int(input("Digite a quantidade actual em estoque: "))
qtd_maxima = int(input("Digite a quantidade máxima em estoque: "))
qtd_minima = int(input("Digite a quantidade mínima em estoque: "))

qtd_media = (qtd_maxima + qtd_minima) / 2

print(f"Quantidade actual em estoque: {qtd_actual} unidade(s)")
print(f"Quantidade máxima em estoque: {qtd_maxima} unidade(s)")
print(f"Quantidade mínima em estoque: {qtd_minima} unidade(s)")
print(f"Quantidade média em estoque: {qtd_media} unidade(s)")

if qtd_actual >= qtd_media:
    print("Não efectuar compra")
else:
    print("Efectuar compra")