import random

def iniciar_tabuleiro(tam):
    tabuleiro = [['.' for _ in range(tam)] for _ in range(tam)]
    return tabuleiro


def posicionar_rainha(tabuleiro):
    linha = random.randint(0, tam-1)
    coluna = random.randint(0, tam-1)
    tabuleiro[linha][coluna] = 'Q'

    return linha, coluna


def imprimir_tabuleiro(tabuleiro):
    for l in range(tam):
        for c in range(tam):
            print(f"{tabuleiro[l][c]}", end=" ")
        print()

#################################


tam = 8

tabuleiro = iniciar_tabuleiro(tam)

pos = posicionar_rainha(tabuleiro)
imprimir_tabuleiro(tabuleiro)