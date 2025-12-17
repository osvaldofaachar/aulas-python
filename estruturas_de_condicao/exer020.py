#Sistema de Classificação Complexo com Aninhados e elif
# Solicitar entrada do usuário
nota = float(input("Digite a nota (0-100): "))
presenca = float(input("Digite a presença (0-100): "))

# Estrutura de decisão com elif e aninhados
if nota >= 90:
    if presenca >= 80:
        print("Aprovado com louvor")
    else:
        print("Reprovado por falta")
elif nota >= 60:
    if presenca >= 75:
        print("Aprovado")
    else:
        print("Reprovado por falta")
else:
    print("Reprovado por nota")