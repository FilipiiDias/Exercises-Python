import tkinter as tk
from tkinter import messagebox
def clique(i, j):
    global jogador_atual
    botao = botoes[i][j]

    if botao["text"] != "":
        return
    
    botao["text"] = jogador_atual

    if verificar_vitoria(jogador_atual):
        messagebox.showinfo("Fim de jogo", f"Parabens! jogador{jogador_atual} VENCEU!!")
        desativar_botoes()
    else:
        jogador_atual = "O" if jogador_atual == "X" else "X"

def verificar_vitoria(jogador):
    # Verifica linhas
    for i in range(3):
        if botoes[i][0]["text"] == jogador and botoes[i][1]["text"] == jogador and botoes[i][2]["text"] == jogador:
            return True

    # Verifica colunas
    for i in range(3):
        if botoes[0][i]["text"] == jogador and botoes[1][i]["text"] == jogador and botoes[2][i]["text"] == jogador:
            return True

    # Verifica diagonais
    if botoes[0][0]["text"] == jogador and botoes[1][1]["text"] == jogador and botoes[2][2]["text"] == jogador:
        return True

    if botoes[0][2]["text"] == jogador and botoes[1][1]["text"] == jogador and botoes[2][0]["text"] == jogador:
        return True

    return False

def desativar_botoes():
    for i in range(3):
        for j in range(3):
            botoes[i][j]["state"] = "disabled"
# Criar janela
janela = tk.Tk()
janela.title("Jogo da velha")
jogador_atual = "X"
botoes = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        botoes[i][j] = tk.Button(janela, text="", width=10, height=4,
                                 command=lambda i=i, j=j: clique(i,j))
        
        botoes[i][j].grid(row = i, column = j)
# Iniciar a janela
janela.mainloop()