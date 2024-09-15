import random


#######################################################


def iniciar_tabuleiro(tam):
    return [[0 for _ in range(tam)] for _ in range(tam)]


#######################################################

def posicionar_primeira_rainha(tabuleiro, tam):
    linha = random.randint(0, tam-1)
    coluna = random.randint(0, tam-1)
    tabuleiro[linha][coluna] = 1
    return linha, coluna



#######################################################



def imprimir_tabuleiro(tabuleiro, tam):
    for l in range(tam):
        for c in range(tam):
            if tabuleiro[l][c] == 1:
                print(" R ", end="")  # Rainha representada por 'R'
            else:
                print(" . ", end="")  # Espaço vazio representado por '.'
        print()  # Pular linha após cada linha do tabuleiro



#######################################################



# Verifica se é seguro posicionar uma rainha na posição (linha, coluna)
def posicao_segura(tabuleiro, linha, coluna, tam):
    # Verifica a linha
    for c in range(tam):
        if tabuleiro[linha][c] == 1:
            return False
    
    # Verifica a coluna
    for l in range(tam):
        if tabuleiro[l][coluna] == 1:
            return False

    # Verifica a diagonal principal
    for i in range(tam):
        if linha - i >= 0 and coluna - i >= 0 and tabuleiro[linha - i][coluna - i] == 1:
            return False
        if linha + i < tam and coluna + i < tam and tabuleiro[linha + i][coluna + i] == 1:
            return False

    # Verifica a diagonal secundária
    for i in range(tam):
        if linha - i >= 0 and coluna + i < tam and tabuleiro[linha - i][coluna + i] == 1:
            return False
        if linha + i < tam and coluna - i >= 0 and tabuleiro[linha + i][coluna - i] == 1:
            return False

    return True



#######################################################



# Backtracking para posicionar as rainhas restantes
def posicionar_rainhas(tabuleiro, rainhas, tam, posicoes):
    if rainhas == 0:
        return True  # Todas as rainhas foram posicionadas

    for linha in range(tam):
        for coluna in range(tam):
            if tabuleiro[linha][coluna] == 0 and posicao_segura(tabuleiro, linha, coluna, tam):
                # Posiciona a rainha
                tabuleiro[linha][coluna] = 1
                posicoes.append((linha, coluna))
                rainhas -= 1

                # Tenta posicionar as próximas rainhas
                if posicionar_rainhas(tabuleiro, rainhas, tam, posicoes):
                    return True

                # Backtracking: remove a rainha e tenta outra posição
                rainhas += 1
                tabuleiro[linha][coluna] = 0
                posicoes.pop()

    return False


#######################################################


# Função principal
def resolver_n_rainhas(tam):
    tabuleiro = iniciar_tabuleiro(tam)
    posicoes = []

    # Posiciona a primeira rainha aleatoriamente
    linha, coluna = posicionar_primeira_rainha(tabuleiro, tam)
    print("primeira posição:\n")
    imprimir_tabuleiro(tabuleiro, tam)
    posicoes.append((linha, coluna))
    rainhas = tam - 1  # Restam N-1 rainhas para posicionar

    # Tenta posicionar as demais rainhas
    if posicionar_rainhas(tabuleiro, rainhas, tam, posicoes):
        print("\nSolução encontrada:\n")
        imprimir_tabuleiro(tabuleiro, tam)
    else:
        print("Nenhuma solução encontrada")



#######################################################

# Main
tam = 8
tabuleiro = iniciar_tabuleiro(tam)

resolver_n_rainhas(tam)