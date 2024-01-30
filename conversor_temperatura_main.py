#conversor_temperatura_main.py

import tkinter as tk
from conversor_temperatura_gui import criar_botao, criar_entry, criar_label
from conversor_temperatura_funcs import converter_para_fahrenheit, converter_para_celsius

def converter_temperatura():
    def converter():
        try:
            valor = float(entrada.get())
            if escolha.get() == "Celsius para Fahrenheit":
                resultado.set(f'{converter_para_fahrenheit(valor):.2f} °F')
            else:
                resultado.set(f"{converter_para_celsius(valor):.2f} °C")
        except ValueError:
            resultado.set("Entrada inválida. Digite um número.")

    janela = tk.Tk()
    janela.title("Conversor de Temperatura")
    janela.geometry("400x200")
    janela.configure(bg='lightblue')

    escolha = tk.StringVar()
    escolha.set("Celsius para Fahrenheit")

    criar_label(janela, "Escolha a conversão: ", 0, 0, tamanho_fonte=14)
    entrada = criar_entry(janela, 1, 0, largura=10)
    criar_botao(janela, "Converter", converter, 2, 0, largura=10, altura=2, cor_fundo="green", cor_texto="white")
    criar_label(janela, "Resultado:", 3, 0, tamanho_fonte=14)
    resultado = tk.StringVar()
    criar_label(janela, "", 4, 0, tamanho_fonte=16).config(textvariable=resultado)

    opcoes = ['Celsius para Fahrenheit', "Fahrenheit para Celsius"]
    menu = tk.OptionMenu(janela, escolha, *opcoes)
    menu.config(width=20)
    menu.grid(row=0, column=1, pady=10)

    janela.mainloop()

converter_temperatura()