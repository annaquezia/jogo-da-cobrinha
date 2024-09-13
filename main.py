"""

"""
import pygame
import random

# Configurações inicias
pygame.init()
pygame.display.set_caption("Jogo da cobrinha")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
timer = pygame.time.Clock()

#   cores RGB
rosa = (245, 202, 194)
vinho = (86, 7, 12)
preto = (0, 0, 0)
verde = (132, 165, 158)

#   parâmentros da cobrinha
tamanho_cobrinha = 20
tamanho_comida = 20
velocidade_jogo = 15


def desenhar_comidinha(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vinho, [comida_x, comida_y, tamanho, tamanho])


def desenhar_cobrinha(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanho, tamanho])


def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Verdana", 15,)
    texto = fonte.render(f"Pontos: {pontuacao}", True, preto)
    tela.blit(texto, [3, 3])


def gerar_comidinha():
    comida_x = round(random.randrange(0, largura - tamanho_comida) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_comida) / 20.0) * 20.0
    return comida_x, comida_y


def selecionar_velocidade(tecla):
    velocidade_x = 0
    velocidade_y = 0
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_cobrinha
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_cobrinha
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_cobrinha
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_cobrinha
        velocidade_y = 0
    return velocidade_x, velocidade_y


# Jogo
def rodar_jogo():
    game_over = False
    x = largura / 2
    y = altura / 2
    velocidade_x = 0
    velocidade_y = 0
    tamanho_inicial = 1
    pixels = []
    comida_x, comida_y = gerar_comidinha()
    while not game_over:
        tela.fill(rosa)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
        desenhar_comidinha(tamanho_comida, comida_x, comida_y)
        if x < 0 or x >= largura or y < 0 or y >= altura:
            game_over = True
        x += velocidade_x
        y += velocidade_y
        pixels.append([x, y])
        if len(pixels) > tamanho_inicial:
            del pixels[0]
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                game_over = True
        desenhar_cobrinha(tamanho_cobrinha, pixels)
        desenhar_pontuacao(tamanho_inicial - 1)
        pygame.display.update()
        if x == comida_x and y == comida_y:
            tamanho_inicial += 1
            comida_x, comida_y = gerar_comidinha()
        timer.tick(velocidade_jogo)


rodar_jogo()
