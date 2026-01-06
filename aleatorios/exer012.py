num_maca = int(input("Digite o número de maçãs compradas: "))

if num_maca < 12:
    maca = 1.50
    total_vendas = num_maca * maca
    print(f"O valor total das maçãs é: {total_vendas}")
else:
    maca = 1.30
    total_vendas = num_maca * maca
    print(f"O valor total das maçãs é: {total_vendas}")
