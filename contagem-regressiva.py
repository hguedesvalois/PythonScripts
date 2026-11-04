from pydoc import text
from time import strptime
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def atualizar_contagem():
    '''
    Calcula e atualiza a contagem na tela
    '''
    data_texto = entrada_data.get()

    try:
        data_alvo = datetime.strptime(data_texto, "%d/%m/%Y %H:%M")
        agora = datetime.now()
        tempo_restante = data_alvo - agora

        # se o tempo acabou
        if tempo_restante.total_seconds() <= 0:
            label_resultado.config(text="O evento chegou!", fg="green")
            return

        # calulos dos formatos corretos de data e hora
        # usando "//" (divisão inteira) e "%" (modulo)
        dias = tempo_restante.days
        segundos_totais = int(tempo_restante.total_seconds())
        segundos = segundos_totais % 60
        minutos = (segundos_totais // 60) % 60
        horas = (segundos_totais // 3600) % 24
        meses = (segundos_totais // 2419200) % 12
        semanas = (segundos_totais // 604800) % 54

        #atualiza texto da janela
        texto_formatado = f"Faltam: {meses} meses, {semanas} semanas, {dias} dias, {horas:02d}h {minutos:02d}m {segundos:02d}s"
        label_resultado.config(text=texto_formatado, fg="black")

        # faz a função rodar novamente depois de 1000 milisegundos
        janela.after(1000, atualizar_contagem)

    except ValueError:
        messagebox.showerror("Erro", "Formato inválido. Use: DD/MM/AAAA HH:MM")

# ---Configuração da janela---
janela = tk.Tk()
janela.title("Contagem Regressiva")
janela.geometry("600x350")

label_instrucao = tk.Label(janela, text= "Digite a data alvo (DD/MM/AAAA HH:MM):", font=("Arial", 11))
label_instrucao.pack(pady=10)

# --- Campo de entrada de Texto ---
entrada_data = tk.Entry(janela, font=("Arial",12), justify="center")
entrada_data.pack(pady=5)

# --- Botao Iniciar ---
botao_iniciar = tk.Button(janela, text="Iniciar", command=atualizar_contagem, font=("Arial",10,"bold"))
botao_iniciar.pack(pady=10)

# --- Botao Fechar ---
botao_sair = tk.Button(janela, text="Sair", command=janela.destroy, font=("Arial", 10, "bold"))
botao_sair.pack(pady=10)

# --- Texto que vai exibir a contagem ---
label_resultado = tk.Label(janela, text="", font=("Arial",16,"bold"))
label_resultado.pack(pady=20)

janela.mainloop()
