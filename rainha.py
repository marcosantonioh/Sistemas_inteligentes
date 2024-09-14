import random

# Função para verificar se a posição (linha, coluna) é segura para colocar uma rainha
def eh_seguro(tabuleiro, linha, coluna, n):
    # Verificar se há uma rainha na mesma coluna
    for i in range(linha):
        if tabuleiro[i][coluna] == 1:
            return False

    # Verificar a diagonal superior esquerda
    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False

    # Verificar a diagonal superior direita
    for i, j in zip(range(linha, -1, -1), range(coluna, n)):
        if tabuleiro[i][j] == 1:
            return False

    return True

# Função para resolver o problema das 8 rainhas utilizando backtracking
def resolver_rainhas(tabuleiro, linha, n):
    if linha >= n:
        return True

    for coluna in range(n):
        if eh_seguro(tabuleiro, linha, coluna, n):
            tabuleiro[linha][coluna] = 1

            if resolver_rainhas(tabuleiro, linha + 1, n):
                return True

            # Backtracking: remover a rainha e tentar a próxima posição
            tabuleiro[linha][coluna] = 0

    return False

# Função para desenhar o tabuleiro de xadrez
def desenhar_tabuleiro(tabuleiro, n):
    for linha in range(n):
        for coluna in range(n):
            if tabuleiro[linha][coluna] == 1:
                print('W', end=' ')
            else:
                print('-', end=' ')
        print()

# Função principal
def main():
    n = 8  # Tamanho do tabuleiro (8x8)
    tabuleiro = [[0 for _ in range(n)] for _ in range(n)]

    # Colocar a primeira rainha em uma posição aleatória na primeira linha
    primeira_coluna = random.randint(0, n - 1)
    tabuleiro[0][primeira_coluna] = 1

    # Resolver o restante do tabuleiro a partir da segunda linha
    if resolver_rainhas(tabuleiro, 1, n):  # Começar da segunda linha
        desenhar_tabuleiro(tabuleiro, n)
    else:
        print("Não há solução.")

if __name__ == "__main__":
    main()
