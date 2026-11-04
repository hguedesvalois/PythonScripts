from datetime import datetime
import time

# Pede a data do usuario
data_usuario = input("Digite a data e hora alvo (Formato: DD/MM/AAAA HH:MM): ")
try:
    data_alvo = datetime.strptime(data_usuario, "%d/%m/%Y %H:%M")

    while True:
        agora = datetime.now()
        tempo_restante = data_alvo - agora

        if tempo_restante == 0:
            print ("\nO evento chegou!")
            break

        # usando os operadores // divisao inteira e % modulo para retornar o tempo que falta no formato adequado
        segundos_totais = int(tempo_restante.total_seconds())
        horas = (segundos_totais // 3600) % 24
        minutos = (segundos_totais // 60) % 60
        segundos = segundos_totais % 60
        semanas = (segundos_totais // 604800) % 54
        meses = (segundos_totais // 2419200) % 12
        dias = tempo_restante.days - (semanas * 7)

        print("--- Contagem Regressiva ---")
        if meses == 0:
            print(f"{semanas} semanas, {dias} dias, {horas:02d}h {minutos:02d}m {segundos:02d}s", end="\n")
        elif meses == 1:
            print(f"{meses} mês, {semanas} semanas, {dias} dias, {horas:02d}h {minutos:02d}m {segundos:02d}s", end="\n")
        elif semanas == 0 and meses == 0:
            print(f"{dias} dias, {horas:02d}h {minutos:02d}m {segundos:02d}s", end="\n")
        elif semanas == 1 and meses == 0:
            print(f"{semanas} semana, {dias} dias, {horas:02d}h {minutos:02d}m {segundos:02d}s", end="\n")
        elif dias == 0 and semanas == 0 and meses == 0:
            print(f"{horas:02d}h {minutos:02d}m {segundos:02d}s", end="\n")
        elif dias == 1 and semanas == 0 and meses == 0:
            print(f"{dias} dia, {horas:02d}h {minutos:02d}m {segundos:02d}s", end="\n")
        else:
            print(f"{meses} meses, {semanas} semanas, {dias} dias, {horas:02d}h {minutos:02d}m {segundos:02d}s", end="\n")

        time.sleep(2)

except ValueError:
    print("\nErro: Formato de data inválido, use DD/MM/AAAA HH:MM.")

except KeyboardInterrupt:
    print("\nContagem interrompida pelo usuário.")
