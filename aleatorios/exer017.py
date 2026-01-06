hora_inicio = int(input("Digite a hora de inicio: "))
hora_fim = int(input("Digite a hora de fim: "))

if hora_inicio < hora_fim:
    duracao = hora_fim - hora_inicio
    print(f"O jogo durou {duracao} horas")
else:
    duracao = hora_inicio - hora_fim
    print(f"O jogo durou {duracao} horas")