anos_digitado = int(input("Quantos anos tens? "))
meses_digitado = int(input("Quantos meses? "))
dias_digitado = int(input("E quantos dias? "))

ano = 365
mes = 30
dia = 1

idade_em_dias = (anos_digitado * ano) + (meses_digitado * mes) + (dias_digitado * dia)

print(f"A idade de {anos_digitado} anos, {meses_digitado} meses e {dias_digitado} dias expressa em dias é: {idade_em_dias}")