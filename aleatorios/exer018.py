horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
salario_por_hora = float(input("Digite o salário por hora: "))

if horas_trabalhadas <= 160:
    salario_final = horas_trabalhadas * salario_por_hora
    print(f"O salário final do funcionário é de {salario_final}")
else:
    salario_final = horas_trabalhadas * salario_por_hora
    percentagem = (salario_final * 50) / 100
    salario_com_horas_extras = salario_final + percentagem
    print(f"O salário final com horas extras do funcionário é de {salario_com_horas_extras}")