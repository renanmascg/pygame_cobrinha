import pygame
from random import randint

# definição de cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

try:
    pygame.init()
except:
    print("Algo de errado ocorreu ao inicializar o python")

largura = 640
altura = 480
tamanho = 10  # pixels

# configuração da janela do jogo
relogio = pygame.time.Clock()  # limitar a quantidade de frames por segundos
fundo = pygame.display.set_mode(size=(largura, altura))
pygame.display.set_caption("Snake")


def cobra(cobraXY):
    for XY in cobraXY:
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])


def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])


def jogo():
    sair = True
    pos_x = randint(0, (largura - tamanho) / 10) * 10
    pos_y = randint(0, (altura - tamanho) / 10) * 10

    maca_x = randint(0, (largura - tamanho) / 10) * 10
    maca_y = randint(0, (altura - tamanho) / 10) * 10

    velocidade_x = 0
    velocidade_y = 0

    while sair:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sair = False

            # eventos de movimentação
            # and -> evita mover em direções opostas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho

                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho

                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho

                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho

        fundo.fill(branco)
        pos_x += velocidade_x
        pos_y += velocidade_y

        cobra_XY = []
        cobra_inicio = []
        cobra_inicio.append(pos_x)
        cobra_inicio.append(pos_y)
        cobra_XY.append(cobra_inicio)

        cobra(cobra_XY)
        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randint(0, (largura - tamanho) / 10) * 10
            maca_y = randint(0, (altura - tamanho) / 10) * 10

        maca(maca_x, maca_y)

        pygame.display.update()
        relogio.tick(15)

        if pos_x > largura:
            pos_x = 0
        if pos_x < 0:
            pos_x = largura - tamanho  # inicia do outro lado

        if pos_y > altura:
            pos_y = 0
        if pos_y < 0:
            pos_y = altura - tamanho

    pygame.display.update()


jogo()
