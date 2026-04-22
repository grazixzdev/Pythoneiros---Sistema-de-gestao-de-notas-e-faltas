Nome = input("Digite o nome do aluno: ")
Matricula = int(input("Digite sua matricula:"))

Mat1 = float(input("Digite sua nota 1 de Matematica:"))
Mat2 = float(input("Digite sua nota 2 de Matematica:"))
MatT = (Mat1 + Mat2)/2
MatP = int(input("Digite a frequencia do aluno: "))

Port1 = float(input("Digite sua nota 1 de Portugues:"))
Port2 = float(input("Digite sua nota 2 de Portugues:"))
PortT = (Port1 + Port2)/2

Ing1 = float(input("Digite sua nota 1 de Ingles:"))
Ing2 = float(input("Digite sua nota 2 de Ingles:"))
IngT = (Ing1 + Ing2)/2

Ed1 = float(input("Digite sua nota 1 de Educação Física:"))
Ed2 = float(input("Digite sua nota 2 de Educação Física:"))
EdT = (Ed1 + Ed2)/2

Art1 = float(input("Digite sua nota 1 de Arte:"))
Art2 = float(input("Digite sua nota 2 de Arte:"))
ArtT = (Art1 + Art2)/2

Fil1 = float(input("Digite sua nota 1 de Filosofia:"))
Fil2 = float(input("Digite sua nota 2 de Filosofia:"))
FilT = (Fil1 + Fil2)/2

Soc1 = float(input("Digite sua nota 1 de Sociologia:"))
Soc2 = float(input("Digite sua nota 2 de Sociologia:"))
SocT = (Soc1 + Soc2)/2

Quim1 = float(input("Digite sua nota 1 de Química:"))
Quim2 = float(input("Digite sua nota 2 de Química:"))
QuimT = (Quim1 + Quim2)/2

Fis1 = float(input("Digite sua nota 1 de Física:"))
Fis2 = float(input("Digite sua nota 2 de Física:"))
FisT = (Fis1 + Fis2)/2

Bio1 = float(input("Digite sua nota 1 de Biologia:"))
Bio2 = float(input("Digite sua nota 2 de Biologia:"))
BioT = (Bio1 + Bio2)/2

faltas = int(input("Digite o numero total de faltas: "))
total_aulas = 80
presenca_percentual = ((total_aulas - faltas) / total_aulas) * 100

media_geral = (MatT + PortT + IngT + EdT + ArtT + FilT + SocT + QuimT + FisT + BioT) / 10

nota_minima = 6.0

situacao = ""
if (presenca_percentual < 75):
    situacao = "Reprovado por falta"
elif (media_geral >= nota_minima):
    situacao = "Aprovado"
else: 
    situacao = "Reprovado por nota"   


print("---------------------------------------------")
print("                Boletim Final                ")
print("---------------------------------------------")
print(f"Ola {Nome}, essas sao suas medias ")
print(f"Sua Matricula:{Matricula}")

print(f"Media Matematica: {MatT}")
print(f"Media Portugues: {PortT}")
print(f"Media Ingles: {IngT}")
print(f"Media Ed Fisica: {EdT}")
print(f"Media Artes: {ArtT}")
print(f"Media Fiolosofia: {FilT}")
print(f"Media Sociologia: {SocT}")
print(f"Media Quimica: {QuimT}")
print(f"Media Fisica: {FisT}")
print(f"Media Biologia: {BioT}")
print(f"Presenca: {presenca_percentual:.2f}%")
print(f"Media Geral: {media_geral:.2f}")
print(f"Situacao Final: {situacao}")

print("---------------------------------------------")

