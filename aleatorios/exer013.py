primeira_nota = float(input("Digite a primeira nota do aluno: "))
segunda_nota = float(input("Digite a segunda nota do aluno: "))

media_do_aluno = (primeira_nota + segunda_nota) / 2

if media_do_aluno >= 6:
    print(f"O aluno foi aprovado com uma média de {media_do_aluno} valores")
else:
    print(f"O aluno foi reprovado com uma média de {media_do_aluno} valores")