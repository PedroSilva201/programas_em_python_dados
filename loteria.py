# Lista dos jogos apostados Creditós Microsoft Copolit
jogos = [
    [1, 3, 13, 15, 20, 58],   # Jogo 1
    [1, 5, 17, 35, 42, 46],   # Jogo 2
    [6, 9, 11, 25, 34, 48],   # Jogo 3
    [7, 11, 20, 24, 37, 42],  # Jogo 4
    [1, 8, 14, 23, 26, 41],   # Jogo 5
    [5, 9, 13, 32, 35, 40],   # Jogo 6
    [4, 8, 13, 32, 35, 40],   # Jogo 7
]

# Números sorteados
sorteio = [4, 8, 15, 16, 23, 42]

# Verificação dos acertos
for i, jogo in enumerate(jogos, start=1):
    acertos = set(jogo) & set(sorteio)  # interseção dos conjuntos
    print(f"Jogo {i}: {jogo}")
    print(f"Acertos: {sorted(list(acertos))} (Total: {len(acertos)})\n")
