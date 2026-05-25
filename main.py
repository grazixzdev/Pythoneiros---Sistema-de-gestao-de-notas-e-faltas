disciplinas = [
    "Matematica", "Portugues", "Ingles", "Educacao Fisica", 
    "Arte", "Filosofia", "Sociologia", "Quimica", "Fisica", "Biologia"
]

CodOn = 1

while (CodOn == 1):
    Nome = input("\nDigite o nome do aluno: ")
    Matricula = int(input("Digite sua matricula: "))
    
    boletim_aluno = {}
    lista_medias = []

    for materia in disciplinas:
        nota1 = float(input(f"Digite a primeira nota de {materia}: "))
        nota2 = float(input(f"Digite a segunda nota de {materia}: "))
        media_materia = (nota1 + nota2) / 2
        
        boletim_aluno[materia] = media_materia
        lista_medias.append(media_materia)

    media_geral = sum(lista_medias) / len(lista_medias)
    faltas = int(input("Digite o numero total de faltas: "))
    total_aulas = 80
    presenca_percentual = ((total_aulas - faltas) / total_aulas) * 100

    nota_minima = 6.0

    reprovou_em_alguma_materia = any(nota < nota_minima for nota in lista_medias)

    situacao = ""
    if (presenca_percentual < 75):
        situacao = "Reprovado por falta"
    elif reprovou_em_alguma_materia:
        situacao = "Reprovado por nota"
    else: 
        situacao = "Aprovado"   


    print("\n---------------------------------------------")
    print("                Boletim Final                ")
    print("---------------------------------------------")
    print(f"Ola {Nome}, essas sao suas medias ")
    print(f"Sua Matricula: {Matricula}")
    print("-" * 45)

    for materia, media_final in boletim_aluno.items():
        print(f"Media {materia}: {media_final:.2f}")

    print("-" * 45)
    print(f"Presenca: {presenca_percentual:.2f}%")
    print(f"Media Geral: {media_geral:.2f}")
    print(f"Situacao Final: {situacao}")
    print("---------------------------------------------")
    
    CodOn = int(input("Deseja continuar cadastrando? (1 - sim / 0 - não): "))