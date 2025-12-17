#Verificar acesso com not e aninhado

# Solicitar entrada do usuário
idade = int(input("Digite sua idade: "))
permissao = input("Digite a permissão (True ou False): ").strip().lower() == "true"  # Converte string para bool

# Estrutura de decisão com if aninhado
if idade >= 18:
    if not (permissao == False):  # Equivale a permissão == True
        print("Acesso")
    else:
        print("Negado")
else:
    print("Negado")