carros_vendidos = int(input("Digite o número de carros vendidos: "))
salario_fixo = float(input("Digite o salário fixo do funcionário: "))
valor_por_carro = float(input("Digite o valor recebido por por carro vendido: "))

valor_vendas = carros_vendidos * valor_por_carro
comissao = (5 * valor_vendas) / 100

salario_final = valor_vendas + salario_fixo + comissao

print(f"O vendedor vendeu {carros_vendidos} carros")
print(f"O salário fixo do vendedor é de {salario_fixo} Mts")
print(f"O valor por carro vendido é de {valor_por_carro} Mts")
print(f"O salário final do vendedor é de {salario_final} Mts")