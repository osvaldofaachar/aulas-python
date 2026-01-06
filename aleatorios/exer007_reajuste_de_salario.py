salario_atual = float(input("Digite o sálario actual do funcionário: "))
percentual_de_reajuste = float(input("Digite o Percentual de Reajuste do Salário: "))

percentual = (percentual_de_reajuste * salario_atual) / 100

salario_ajustado = salario_atual + percentual

print(f"O Salário Actual do Funcionário é: {salario_atual} Mts \n"
      f"O Percentual de Reajuste Foi de {percentual_de_reajuste}% \n"
      f"O Salário Final do Funcionário é: {salario_ajustado} Mts")