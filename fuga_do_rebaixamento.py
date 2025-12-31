import itertools
from collections import defaultdict

# ==============================
# CONFIGURAÇÕES
# ==============================
# Pontos após 37 jogos
pontos_iniciais = {
    "A": 45,
    "B": 44,
    "C": 43,
    "D": 43,
    "E": 42,
    "F": 41,
}

# Última rodada: cada equipe enfrenta um adversário externo (não listado aqui)
# Tratamos apenas o resultado da equipe (3/1/0) como no simulador do título
pontos_por_resultado = [3, 1, 0]  # vitória, empate, derrota

# Critérios de desempate (placeholder):
# Substitua por sua regra real: saldo de gols, vitórias, confronto direto, etc.
# Aqui, se houver empate em pontos, mantemos a ordem alfabética como estável (apenas para quebrar empate no relatório).
def ordenar_classificacao(pontos_finais):
    # Ordena por pontos desc e, em caso de empate, pelo nome para estabilidade (substituir por critérios reais)
    return sorted(pontos_finais.items(), key=lambda kv: (-kv[1], kv[0]))

# ==============================
# SIMULAÇÃO
# ==============================
equipes = list(pontos_iniciais.keys())

# Todas as combinações de resultados possíveis (3 opções por equipe)
# Exemplo de uma combinação: [3,1,0,3,1,0] significa:
# A venceu (3), B empatou (1), C perdeu (0), D venceu (3), E empatou (1), F perdeu (0)
todas_combinacoes = list(itertools.product(pontos_por_resultado, repeat=len(equipes)))
total_cenarios = len(todas_combinacoes)

# Contagem de pares rebaixados (os dois últimos)
cenarios_rebaixados = defaultdict(int)

for combo in todas_combinacoes:
    pontos = pontos_iniciais.copy()
    # Aplica resultado independente por equipe
    for equipe, ganho in zip(equipes, combo):
        pontos[equipe] += ganho

    # Ordena classificação aplicando critérios (placeholder)
    tabela = ordenar_classificacao(pontos)

    # Identifica os dois últimos
    ultimos_dois = [tabela[-2][0], tabela[-1][0]]
    chave = tuple(sorted(ultimos_dois))
    cenarios_rebaixados[chave] += 1

# ==============================
# RELATÓRIO
# ==============================
print(f"Total de combinações simuladas: {total_cenarios}")

# Distribuição dos pares rebaixados (do mais frequente ao menos)
distribuicao = sorted(cenarios_rebaixados.items(), key=lambda kv: kv[1], reverse=True)
for pares, qtd in distribuicao:
    perc = 100 * qtd / total_cenarios
    print(f"Rebaixados: {pares} -> {qtd} cenários ({perc:.2f}%)")
# NOVA PARTE
import itertools

# ==============================
# CONFIGURAÇÕES
# ==============================
# Pontos após 37 jogos
pontos_iniciais = {
    "A": 45,
    "B": 44,
    "C": 43,
    "D": 43,
    "E": 42,
    "F": 41,
}

# Resultados possíveis na última rodada por equipe
# W=vitória (3), D=empate (1), L=derrota (0)
resultado_para_pontos = {"W": 3, "D": 1, "L": 0}
resultados_possiveis = ["W", "D", "L"]

equipes = ["A", "B", "C", "D", "E", "F"]

# Critério de desempate placeholder: ordem alfabética (substitua por seus critérios reais)
def ordenar_classificacao(pontos_finais):
    # Ordena por pontos (desc), e desempata por nome (asc) para estabilidade
    return sorted(pontos_finais.items(), key=lambda kv: (-kv[1], kv[0]))

# ==============================
# GERAÇÃO DE CENÁRIOS
# ==============================
todas_combinacoes = list(itertools.product(resultados_possiveis, repeat=len(equipes)))
total_cenarios = len(todas_combinacoes)

print(f"Total de combinações simuladas: {total_cenarios}\n")

for idx, combo in enumerate(todas_combinacoes, start=1):
    # Aplica resultados por equipe
    pontos = pontos_iniciais.copy()
    resultados_equipes = {}
    for equipe, res in zip(equipes, combo):
        ganho = resultado_para_pontos[res]
        pontos[equipe] += ganho
        resultados_equipes[equipe] = res

    # Ordena classificação
    tabela = ordenar_classificacao(pontos)

    # Identifica os dois últimos
    ultimos_dois = [tabela[-2][0], tabela[-1][0]]

    # Formata saída por equipe
    resultados_fmt = ", ".join(
        f"{equipe}:{resultados_equipes[equipe]}({pontos[equipe]})" for equipe in equipes
    )

    print(f"Cenário {idx:03d}: [{resultados_fmt}] -> Rebaixados: {ultimos_dois[0]} e {ultimos_dois[1]}")

