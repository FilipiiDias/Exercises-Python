## Jogo da velha em python 


def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tab, jogador):
    # vericar linhas
    for i in range(3):
        if tab[i][0] == jogador and tab[i][1] == jogador and tab[i][2] == jogador:
            return True
    # vericar colunas
    for i in range(3):
        if tab[0][i] == jogador and tab[1][i] == jogador and tab[2][i] == jogador:
            return True
    if tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador:
        return True
    if tab[0][2] == jogador and  tab[1][1] == jogador and tab[2][0] == jogador:
        return True
    return False
tabuleiro = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]
jogador_atual = "X"

for rodada in range(9):
    mostrar_tabuleiro(tabuleiro)
    escolha = input(f"jogador {jogador_atual}, escolha uma posicao de (1-9):")
    pos = int(escolha) - 1
    linha, coluna = pos // 3, pos% 3
    if tabuleiro[linha][coluna] in ["X", "O"]:
        print("Posicao ja ocupada, tente novamente")
        continue

    tabuleiro[linha][coluna] = jogador_atual

    if verificar_vitoria(tabuleiro, jogador_atual):
        print(f"Jogador {jogador_atual} VENCEU!!")
        break

    if jogador_atual == "O":
        jogador_atual == "X"
    else:
        jogador_atual = "O"
mostrar_tabuleiro(tabuleiro)