# =================================================================
# PROJETO: SISTEMA DE GESTÃO DE NOTAS E FALTAS (ETAPA 3)
# CONTEÚDO: Estruturas de Decisão (if, elif, else)
# =================================================================

def cadastro_notas (relatorio_detalhado, disciplinas, total_aulas, nota_minima):
    for materia in disciplinas:
        print(f"\nDISCIPLINA: {materia}")
        
        # Lançamento do 1º Bimestre (Prova 6.0 + Atividades 4.0)
        p1 = float(input(f"  Nota da Prova - 1º Bim (0-6): "))
        a1 = float(input(f"  Nota de Atividades - 1º Bim (0-4): "))
        nota_bim1 = p1 + a1
        
        # Lançamento do 2º Bimestre (Prova 6.0 + Atividades 4.0)
        p2 = float(input(f"  Nota da Prova - 2º Bim (0-6): "))
        a2 = float(input(f"  Nota de Atividades - 2º Bim (0-4): "))
        nota_bim2 = p2 + a2
        
        # Cálculo da Média Final e Frequência
        media_final = (nota_bim1 + nota_bim2) / 2
        faltas = int(input(f"  Total de faltas em {materia}: "))
        presenca_percentual = ((total_aulas - faltas) / total_aulas) * 100

        situacao = situacao_materia(presenca_percentual, media_final, nota_minima)
        
        # Armazenando os dados da disciplina para o relatório
        relatorio_detalhado += (
            f"Matéria: {materia:.<20} | Média: {media_final:>4.1f} | "
            f"Frequência: {presenca_percentual:>5.1f}% | Situação: {situacao}\n"
        )
    return relatorio_detalhado


def situacao_materia (presenca_percentual, media_final, nota_minima):
    # -------------------------------------------------------------
    # ETAPA 3: ESTRUTURA DE DECISÃO (Lógica de Aprovação/Reprovação)
    # -------------------------------------------------------------
    if presenca_percentual < 75:
        situacao = "REPROVADO POR FALTA"
    elif media_final >= nota_minima:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO POR NOTA"
    return(situacao)

def relatorio_final (nome, matricula, nivel_ensino, relatorio_detalhado):
    # -------------------------------------------------------------
    # RELATÓRIO FINAL
    # -------------------------------------------------------------
    print("\n" + "="*70)
    print(f"{'RELATÓRIO DE RENDIMENTO ESCOLAR':^70}")
    print("="*70)
    print(f"ALUNO: {nome}")
    print(f"MATRÍCULA: {matricula}")
    print(f"NÍVEL: {nivel_ensino}")
    print("-" * 70)
    print(relatorio_detalhado)
    print("="*70)
    print("Sistema processado de acordo com a Lei nº 9.394/1996 (LDB).")

# -------------------------------------------------------------
# INICIO DO FLUXO PRINCIPAL
# -------------------------------------------------------------

print("--- CADASTRO ACADÊMICO - EDUCAÇÃO BÁSICA ---")

# 1. Cadastro de Informações Gerais
nome = input("Digite o nome do aluno: ")
matricula = input("Digite a matrícula: ")
nivel_ensino = "Ensino Médio"  # Definido com base nas disciplinas fornecidas
total_aulas = 80  # Exemplo: total de aulas ministradas no semestre/ano
nota_minima = 6.0

# Lista de disciplinas para processamento
disciplinas = [
    "Matemática", "Português", "Inglês", "Educação Física", "Arte",
    "Filosofia", "Sociologia", "Química", "Física", "Biologia"
]

print(f"\nIniciando lançamento de notas para: {nome}")
print("-" * 50)

# O relatório final será acumulado nesta string
relatorio_detalhado = ""

# Loop para processar cada disciplina (Uso de lista para otimizar o código da Etapa 2)
relatorio_detalhado = cadastro_notas(relatorio_detalhado, disciplinas, total_aulas, nota_minima)

relatorio_final(nome, matricula, nivel_ensino, relatorio_detalhado)
