numero_de_eleitores = int(input("Digite o número total de eleitores: "))
votos_brancos = int(input("Digite o número total de votos em branco: "))
votos_nulos = int(input("Digite o número total de votos nulos: "))

per_votos_brancos = (100 * votos_brancos) / numero_de_eleitores
per_votos_nulos = (100 * votos_nulos) / numero_de_eleitores
votos_validos = numero_de_eleitores - votos_nulos - votos_brancos
per_votos_validos = (100 * votos_validos) / numero_de_eleitores


print(f"O Município tem um total de {numero_de_eleitores} cidadãos")
print(f"Votos Nulos: {votos_nulos} (representam {per_votos_nulos:.1f}% dos cidadãos desde município)")
print(f"Votos Em Branco: {votos_brancos} (representam {per_votos_brancos:.1f}% dos cidadãos desde município)")
print(f"Votos Válidos: {votos_validos} (representam {per_votos_validos:.1f}% dos cidadãos desde município)")