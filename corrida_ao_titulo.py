# Versão Antiga
# Programa 1: Onde calcula a combinação cenario a cenario de cada equipe, jogo a jogo
# Creditos: Microsoft Copilot, 
import itertools

# Pontos iniciais
pontos_A = 74
pontos_B = 70

# Cenários possíveis por rodada (A,B)
cenarios = [
    (3,3), (3,1), (3,0),
    (1,3), (1,1), (1,0),
    (0,3), (0,1), (0,0)
]

def vencedor_em_rodada(combinacao):
    """Verifica rodada a rodada quando o vencedor é definido"""
    pontosA = pontos_A
    pontosB = pontos_B
    for rodada, (pa, pb) in enumerate(combinacao, start=36):
        pontosA += pa
        pontosB += pb
        # Máximo que cada equipe ainda pode alcançar
        max_pontos_B = pontosB + (38 - rodada) * 3
        max_pontos_A = pontosA + (38 - rodada) * 3
        if pontosA > max_pontos_B:
            return f"Equipe A campeã garantida na rodada {rodada}"
        elif pontosB > max_pontos_A:
            return f"Equipe B campeã garantida na rodada {rodada}"
    # Se só define no final
    if pontosA > pontosB:
        return "Equipe A campeã na rodada 38"
    elif pontosB > pontosA:
        return "Equipe B campeã na rodada 38"
    else:
        return "Empate na rodada 38"

# Gerar todas as combinações possíveis até a rodada 38
combinacoes = list(itertools.product(cenarios, repeat=3))

# Mostrar alguns exemplos
for i, comb in enumerate(combinacoes[:729], start=1):  # só os 15 primeiros para não lotar a tela
    pontos_finais_A = pontos_A + sum(r[0] for r in comb)
    pontos_finais_B = pontos_B + sum(r[1] for r in comb)
    decisao = vencedor_em_rodada(comb)
    print(f"Cenário {i}: {comb} -> A:{pontos_finais_A}, B:{pontos_finais_B} => {decisao}")

print(f"\nTotal de combinações geradas: {len(combinacoes)}")

# Programa 2
# Calcular o cenario de percentual das combinações das equipes e de quem irá ser campeão
import itertools

# Pontos iniciais
pontos_A = 74
pontos_B = 70

# Cenários possíveis por rodada (A,B)
cenarios = [
    (3,3), (3,1), (3,0),
    (1,3), (1,1), (1,0),
    (0,3), (0,1), (0,0)
]

def vencedor_em_rodada(combinacao):
    """Verifica rodada a rodada quando o vencedor é definido"""
    pontosA = pontos_A
    pontosB = pontos_B
    for rodada, (pa, pb) in enumerate(combinacao, start=36):
        pontosA += pa
        pontosB += pb
        # Máximo que cada equipe ainda pode alcançar
        max_pontos_B = pontosB + (38 - rodada) * 3
        max_pontos_A = pontosA + (38 - rodada) * 3
        if pontosA > max_pontos_B:
            return "A", rodada
        elif pontosB > max_pontos_A:
            return "B", rodada
    # Se só define no final
    if pontosA > pontosB:
        return "A", 38
    elif pontosB > pontosA:
        return "B", 38
    else:
        return "E", 38  # Empate

# Gerar todas as combinações possíveis até a rodada 38
combinacoes = list(itertools.product(cenarios, repeat=3))

# Estatísticas
rodada_stats = {36:0, 37:0, 38:0}
resultado_stats = {"A":0, "B":0, "E":0}

for comb in combinacoes:
    vencedor, rodada = vencedor_em_rodada(comb)
    rodada_stats[rodada] += 1
    resultado_stats[vencedor] += 1

total = len(combinacoes)

# Mostrar estatísticas consolidadas
print("=== Estatísticas por rodada ===")
for rodada in rodada_stats:
    qtd = rodada_stats[rodada]
    perc = (qtd/total)*100
    print(f"Rodada {rodada}: {qtd} cenários ({perc:.2f}%)")

print("\n=== Estatísticas por equipe ===")
for equipe in resultado_stats:
    qtd = resultado_stats[equipe]
    perc = (qtd/total)*100
    nome = "Equipe A" if equipe=="A" else "Equipe B" if equipe=="B" else "Empate"
    print(f"{nome}: {qtd} cenários ({perc:.2f}%)")


# Versão Nova4
# Parte 1 do Programa
import itertools

# Pontos iniciais (após 36 jogos)
pontos_A = 75
pontos_B = 70

# Cenários possíveis por rodada (A,B)
cenarios = [
    (3,3), (3,1), (3,0),
    (1,3), (1,1), (1,0),
    (0,3), (0,1), (0,0)
]

def vencedor_em_rodada(combinacao):
    """Verifica rodada a rodada quando o vencedor é definido"""
    pontosA = pontos_A
    pontosB = pontos_B
    for rodada, (pa, pb) in enumerate(combinacao, start=37):  # começa na 37ª rodada
        pontosA += pa
        pontosB += pb
        # Máximo que cada equipe ainda pode alcançar
        max_pontos_B = pontosB + (38 - rodada) * 3
        max_pontos_A = pontosA + (38 - rodada) * 3
        if pontosA > max_pontos_B:
            return f"Equipe A campeã garantida na rodada {rodada}"
        elif pontosB > max_pontos_A:
            return f"Equipe B campeã garantida na rodada {rodada}"
    # Se só define no final
    if pontosA > pontosB:
        return "Equipe A campeã na rodada 38"
    elif pontosB > pontosA:
        return "Equipe B campeã na rodada 38"
    else:
        return "Empate na rodada 38"

# Gerar todas as combinações possíveis (2 rodadas → 81 cenários)
combinacoes = list(itertools.product(cenarios, repeat=2))

# Mostrar todas as combinações (81 cenários)
for i, comb in enumerate(combinacoes, start=1):
    pontos_finais_A = pontos_A + sum(r[0] for r in comb)
    pontos_finais_B = pontos_B + sum(r[1] for r in comb)
    decisao = vencedor_em_rodada(comb)
    print(f"Cenário {i}: {comb} -> A:{pontos_finais_A}, B:{pontos_finais_B} => {decisao}")

print(f"\nTotal de combinações geradas: {len(combinacoes)}")

# Parte 2 do Programa
import itertools

# Pontos iniciais (após 36 jogos)
pontos_A = 75
pontos_B = 70

# Cenários possíveis por rodada (A,B)
cenarios = [
    (3,3), (3,1), (3,0),
    (1,3), (1,1), (1,0),
    (0,3), (0,1), (0,0)
]

def vencedor_em_rodada(combinacao):
    """Verifica rodada a rodada quando o vencedor é definido"""
    pontosA = pontos_A
    pontosB = pontos_B
    for rodada, (pa, pb) in enumerate(combinacao, start=37):  # começa na 37ª
        pontosA += pa
        pontosB += pb
        # Máximo que cada equipe ainda pode alcançar
        max_pontos_B = pontosB + (38 - rodada) * 3
        max_pontos_A = pontosA + (38 - rodada) * 3
        if pontosA > max_pontos_B:
            return "A", rodada
        elif pontosB > max_pontos_A:
            return "B", rodada
    # Se só define no final
    if pontosA > pontosB:
        return "A", 38
    elif pontosB > pontosA:
        return "B", 38
    else:
        return "E", 38  # Empate

# Gerar todas as combinações possíveis (2 rodadas → 81 cenários)
combinacoes = list(itertools.product(cenarios, repeat=2))

# Estatísticas
rodada_stats = {37:0, 38:0}
resultado_stats = {"A":0, "B":0, "E":0}

for comb in combinacoes:
    vencedor, rodada = vencedor_em_rodada(comb)
    rodada_stats[rodada] += 1
    resultado_stats[vencedor] += 1

total = len(combinacoes)

# Mostrar estatísticas consolidadas
print("=== Estatísticas por rodada ===")
for rodada in rodada_stats:
    qtd = rodada_stats[rodada]
    perc = (qtd/total)*100
    print(f"Rodada {rodada}: {qtd} cenários ({perc:.2f}%)")

print("\n=== Estatísticas por equipe ===")
for equipe in resultado_stats:
    qtd = resultado_stats[equipe]
    perc = (qtd/total)*100
    nome = "Equipe A" if equipe=="A" else "Equipe B" if equipe=="B" else "Empate"
    print(f"{nome}: {qtd} cenários ({perc:.2f}%)")

print(f"\nTotal de combinações simuladas: {total}")
