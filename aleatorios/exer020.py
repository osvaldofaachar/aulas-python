numero_conta = int(input("Digite o número da conta: "))
saldo_inicial = float(input("Digite o saldo inicial da conta: "))
valor_debito = float(input("Digite o valor de débito da conta: "))
valor_credito = float(input("Digite o valor de crédito da conta: "))

saldo_actual = saldo_inicial - valor_debito + valor_credito

print(f"Número da Conta: {numero_conta}.")
print(f"Saldo Inicial da Conta: {saldo_inicial} Mts")
print(f"Valor de Débito da Conta: {valor_debito} Mts")
print(f"Valor de Crédito da Conta: {valor_credito}")
print(f"Saldo Actual da Conta: {saldo_actual} Mts")

if saldo_actual >= 0:
    print("SALDO POSITIVO")
else:
    print("SALDO NEGATIVO")