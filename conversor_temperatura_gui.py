#conversor_temperatura_gui.py

import tkinter as tk
from conversor_temperatura_funcs import converter_para_celsius, converter_para_fahrenheit

def criar_botao(janela, texto, comando, linha, coluna, colunas_span=1, largura=10, altura=2, cor_fundo='lightgray', cor_texto = 'black' ):
    botao = tk.Button(janela, text=texto, command=comando, width=largura, height=altura, bg=cor_fundo, fg=cor_texto)
    botao.grid(row=linha, column=coluna, columnspan=colunas_span, padx=5, pady=5)
    return botao

def criar_label(janela, texto, linha, coluna, colunas_span=1, tamanho_fonte=12):
    label = tk.Label(janela, text=texto, font=("Arial", tamanho_fonte))
    label.grid(row=linha, column=coluna, columnspan=colunas_span, pady=5)
    return label

def criar_entry(janela, linha, coluna, colunas_span=1, largura=10):
    entry = tk.Entry(janela, width=largura, font=("Ariel, 14"))
    entry.grid(row=linha, column=coluna, columnspan=colunas_span, pady=5)
    return entry