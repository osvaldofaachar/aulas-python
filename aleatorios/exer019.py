salario_fixo = float(input("Digite o salário fixo do vendedor: "))
valor_de_vendas = float(input("Digite o valor de vendas do vendedor: "))

if valor_de_vendas <= 1500:
    comissao = (valor_de_vendas * 3) / 100
    salario_final = salario_fixo + comissao
    print(f"O valor de vendas do vendedor é {valor_de_vendas} Mts")
    print(f"A comissão de 3% no total de vendas é {comissao} Mts")
    print(f"O salário final do vendedor é de {salario_final} Mts")
else:
    comissao = (valor_de_vendas * 5) / 100
    salario_final = salario_fixo + comissao
    print(f"O valor de vendas do vendedor é {valor_de_vendas} Mts")
    print(f"A comissão de 5% no total de vendas é {comissao} Mts")
    print(f"O salário final do vendedor é de {salario_final} Mts")