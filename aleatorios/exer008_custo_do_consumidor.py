custo_de_fabrica = float(input("Digite o custo de fábrica do carro: "))

percentual_distribuidor = (28 * custo_de_fabrica) / 100
percentual_de_impostos = (45 * custo_de_fabrica) / 100

valor_total = custo_de_fabrica + percentual_de_impostos + percentual_distribuidor

print(f"O Custo de Fábrica do Carro Corresponde à: {custo_de_fabrica}")
print(f"O percentagem do distribuidor é de 28% que corresponde à {percentual_distribuidor} Mts")
print(f"O percentagem dos impostos é de 45% que corresponde à {percentual_de_impostos} Mts")
print(f"O valor total do custo do carro novo é: {valor_total} Mts")