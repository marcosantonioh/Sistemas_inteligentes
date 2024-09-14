import numpy as np
import matplotlib.pyplot as plt
import random




def criar_matriz(tam, total_obs):
    matriz = np.zeros((tam, tam))  # 0 representa espaço livre (branco)
    num_obstaculos = int((total_obs / 100) * (tam * tam))
    
    # Gerar posições aleatórias para os obstáculos
    obstaculos = random.sample([(i, j) for i in range(tam) for j in range(tam)], num_obstaculos)
    
    # Colocar obstáculos na matriz
    for (i, j) in obstaculos:
        matriz[i, j] = 1  # 1 representa obstáculo (preto)
    
    return matriz, obstaculos





def posicionar_robo(matriz):
    tam = matriz.shape[0]
    while True:
        x, y = random.randint(0, tam-1), random.randint(0, tam-1)
        if matriz[x, y] == 0:  # Garantir que o robô não seja posicionado em um obstáculo
            return (x, y)





def plotar_matriz(matriz, pos_robo):
    tam = matriz.shape[0]
    fig, ax = plt.subplots()
    
    # Desenhar obstáculos e espaços livres
    for i in range(tam):
        for j in range(tam):
            if matriz[i, j] == 1:
                ax.add_patch(plt.Rectangle((j, tam-i-1), 1, 1, color="black"))  # Obstáculos (quadrados pretos)
    
    # Desenhar o robô (círculo vermelho)
    ax.add_patch(plt.Circle((pos_robo[1] + 0.5, tam - pos_robo[0] - 0.5), 0.3, color='red'))

    # Configuração do gráfico
    ax.set_xlim(0, tam)
    ax.set_ylim(0, tam)
    ax.set_xticks(np.arange(0, tam, 1))
    ax.set_yticks(np.arange(0, tam, 1))
    ax.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Exibir o gráfico
    plt.show()





# Parâmetros
tam_matriz = 7  # Defina o tam da matriz (ex: 10x10)
total_obs = 5  # Defina a porcentagem de obstáculos (ex: 20%)

# Criar a matriz com obstáculos
matriz, obstaculos = criar_matriz(tam_matriz, total_obs)

# Posicionar o robô
pos_robo = posicionar_robo(matriz)

# Plotar a matriz com o robô
plotar_matriz(matriz, pos_robo)
