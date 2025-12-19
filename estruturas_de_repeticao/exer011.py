senha_correcta = "123123"
senha = ""

while senha != senha_correcta:
    senha = input("Digite a sua senha: ")
    if senha != senha_correcta:
        print("Senha Incorrecta. Tente Novamente.")
print("Acesso Concedido!")