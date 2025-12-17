#Verificar login com and/or

usuario = input("Digite o seu usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "123":
    print(f"Seja bem vindo {usuario}")
else:
    print("Senha ou usuário icorrectos.")