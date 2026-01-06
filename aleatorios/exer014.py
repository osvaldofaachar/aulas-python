ano_actual = int(input("Digite o ano actual: "))
ano_de_nascimento = int(input("Digite o seu ano de nascimento: "))

idade = ano_actual - ano_de_nascimento

if idade >= 18:
    print(f"SUA IDADE É {idade} ANOS, ENTÃO PODE VOTAR")
else:
    print(f"SUA IDADE É {idade} ANOS, ENTÃO NÃO PODE VOTAR")