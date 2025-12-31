# Horario Fixo
from datetime import datetime, timedelta

inicio = datetime.strptime("05:00", "%H:%M")
fim = datetime.strptime("00:00", "%H:%M") + timedelta(days=1)  # meia-noite
intervalo = timedelta(minutes=10)

horarios = []
atual = inicio
while atual < fim:
    horarios.append(atual.strftime("%H:%M"))
    atual += intervalo

print("Total de viagens:", len(horarios))
print("Horários:", horarios)

# Frequencia por horario
from datetime import datetime, timedelta

def gerar_horarios(inicio_str, fim_str, intervalo_min):
    inicio = datetime.strptime(inicio_str, "%H:%M")
    fim = datetime.strptime(fim_str, "%H:%M")
    if fim <= inicio:  # se for meia-noite, ajusta para o dia seguinte
        fim += timedelta(days=1)
    intervalo = timedelta(minutes=intervalo_min)
    
    horarios = []
    atual = inicio
    while atual < fim:
        horarios.append(atual.strftime("%H:%M"))
        atual += intervalo
    return horarios
----------------------------------------------------------------------------------------
# Definição das faixas
faixas = [
    ("05:00", "09:00", 40),
    ("09:00", "16:00", 80),
    ("16:00", "20:00", 40),
    ("20:00", "00:00", 80),
]

# Geração dos horários
todos_horarios = []
for inicio, fim, intervalo in faixas:
    todos_horarios.extend(gerar_horarios(inicio, fim, intervalo))

print("Total de viagens:", len(todos_horarios))
print("Horários:", todos_horarios)

# Espera do usuario no ponto
from datetime import datetime, timedelta

# Função para gerar horários (intervalo fixo)
def gerar_horarios(inicio_str, fim_str, intervalo_min):
    inicio = datetime.strptime(inicio_str, "%H:%M")
    fim = datetime.strptime(fim_str, "%H:%M")
    if fim <= inicio:  # ajusta se fim for meia-noite
        fim += timedelta(days=1)
    intervalo = timedelta(minutes=intervalo_min)
    
    horarios = []
    atual = inicio
    while atual < fim:
        horarios.append(atual)
        atual += intervalo
    return horarios

# Lista de horários da linha (exemplo: intervalo fixo de 80 min)
horarios = gerar_horarios("05:00", "00:00", 80)

# Função para encontrar próximo ônibus
def proximo_onibus(horarios, hora_atual_str):
    hora_atual = datetime.strptime(hora_atual_str, "%H:%M")
    for h in horarios:
        if h.time() >= hora_atual.time():
            return h.strftime("%H:%M")
    return "Não há mais ônibus hoje."

# Teste
print("Próximo ônibus às 14:35:", proximo_onibus(horarios, "14:35"))
print("Próximo ônibus às 19:35:", proximo_onibus(horarios, "19:35"))# agora
print("Próximo ônibus às 23:50:", proximo_onibus(horarios, "23:50"))

# Programa Completo
from datetime import datetime, timedelta

# Função para gerar horários em uma faixa
def gerar_horarios(inicio_str, fim_str, intervalo_min):
    inicio = datetime.strptime(inicio_str, "%H:%M")
    fim = datetime.strptime(fim_str, "%H:%M")
    if fim <= inicio:  # ajusta se fim for meia-noite
        fim += timedelta(days=1)
    intervalo = timedelta(minutes=intervalo_min)
    
    horarios = []
    atual = inicio
    while atual < fim:
        horarios.append(atual)
        atual += intervalo
    return horarios

# Definição das faixas de operação (pico e normal)
faixas = [
    ("05:00", "09:00", 40),  # pico da manhã
    ("09:00", "16:00", 80),  # normal
    ("16:00", "20:00", 40),  # pico da tarde
    ("20:00", "00:00", 80),  # normal noite
]

# Geração de todos os horários do dia
todos_horarios = []
for inicio, fim, intervalo in faixas:
    todos_horarios.extend(gerar_horarios(inicio, fim, intervalo))

# Função para encontrar próximo ônibus
def proximo_onibus(horarios, hora_atual_str):
    hora_atual = datetime.strptime(hora_atual_str, "%H:%M")
    for h in horarios:
        if h.time() >= hora_atual.time():
            return h.strftime("%H:%M")
    return "Não há mais ônibus hoje."

# Programa principal
print("Bem-vindo ao simulador da linha 410 ")
hora_usuario = input("Digite o horário atual (HH:MM): ")
print("Próximo ônibus:", proximo_onibus(todos_horarios, hora_usuario))

# Programa completo com tempo de espera:
from datetime import datetime, timedelta

# Função para gerar horários em uma faixa
def gerar_horarios(inicio_str, fim_str, intervalo_min):
    inicio = datetime.strptime(inicio_str, "%H:%M")
    fim = datetime.strptime(fim_str, "%H:%M")
    if fim <= inicio:  # ajusta se fim for meia-noite
        fim += timedelta(days=1)
    intervalo = timedelta(minutes=intervalo_min)
    
    horarios = []
    atual = inicio
    while atual < fim:
        horarios.append(atual)
        atual += intervalo
    return horarios

# Definição das faixas de operação (pico e normal)
faixas = [
    ("05:00", "09:00", 40),  # pico da manhã
    ("09:00", "16:00", 80),  # normal
    ("16:00", "20:00", 40),  # pico da tarde
    ("20:00", "00:00", 80),  # normal noite
]

# Geração de todos os horários do dia
todos_horarios = []
for inicio, fim, intervalo in faixas:
    todos_horarios.extend(gerar_horarios(inicio, fim, intervalo))

# Função para encontrar próximo ônibus e tempo de espera
def proximo_onibus(horarios, hora_atual_str):
    hora_atual = datetime.strptime(hora_atual_str, "%H:%M")
    for h in horarios:
        if h.time() >= hora_atual.time():
            espera = (h - hora_atual).seconds // 60  # diferença em minutos
            return h.strftime("%H:%M"), espera
    return None, None

# Programa principal
print("Bem-vindo ao simulador da linha 410")
hora_usuario = input("Digite o horário atual (HH:MM): ")
proximo, espera = proximo_onibus(todos_horarios, hora_usuario)

if proximo:
    print(f"Próximo ônibus: {proximo}")
    print(f"Tempo de espera: {espera} minutos")
else:
    print("Não há mais ônibus hoje.")

# Desvio Padrão
import statistics

# Intervalos reais observados (em minutos)
intervalos_pico = [38, 42, 41, 39, 45, 45, 51]

media = statistics.mean(intervalos_pico)
desvio = statistics.stdev(intervalos_pico)

print(f"Média dos intervalos: {media:.2f} min")
print(f"Desvio padrão: {desvio:.2f} min")

# Frequencia
def calcular_frequencia(intervalo_min):
    return 60 / intervalo_min

intervalos = [40, 80]
for i in intervalos:
    freq = calcular_frequencia(i)
    print(f"Intervalo: {i} min -> Frequência: {freq:.2f} ônibus/hora")
