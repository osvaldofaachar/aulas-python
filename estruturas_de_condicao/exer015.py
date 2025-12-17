#Verificar nível de bateria com elif

percentagem = int(input("Digite uma percentagem de 1 - 100: "))

if percentagem < 20:
    print("CRITICA")
elif percentagem < 50:
    print("BAIXA")
else:
    print("BOA")