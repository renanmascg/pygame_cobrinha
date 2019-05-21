import pygame
from random import randrange

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

largura = 320
altura = 280
tamanho = 10  # pixels
placar = 40

# configuração da janela do jogo
relogio = pygame.time.Clock()  # limitar a quantidade de frames por segundos
fundo = pygame.display.set_mode(size=(largura, altura))
pygame.display.set_caption("Snake")


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])


def cobra(cobraXY):
    for XY in cobraXY:
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])


def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])


def jogo():
    sair = True
    fim_de_jogo = False
    pos_x = randrange(0, (largura - tamanho), 10)
    pos_y = randrange(0, (altura - tamanho), 10)

    maca_x = randrange(0, (largura - tamanho), 10)
    maca_y = randrange(0, (altura - tamanho - placar), 10)

    velocidade_x = 0
    velocidade_y = 0

    cobra_XY = []
    cobra_comp = 1

    while sair:

        while fim_de_jogo:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fim_de_jogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = True
                        fim_de_jogo = False
                        pos_x = randrange(0, (largura - tamanho), 10)
                        pos_y = randrange(0, (altura - tamanho), 10)

                        maca_x = randrange(0, (largura - tamanho), 10)
                        maca_y = randrange(0, (altura - tamanho), 10)

                        velocidade_x = 0
                        velocidade_y = 0

                        cobra_XY = []
                        cobra_comp = 1

                    if event.key == pygame.K_s:
                        sair = False
                        fim_de_jogo = False

            fundo.fill(branco)
            texto("FIM DE JOGO", vermelho, 50, 55, 30)
            texto("PONTUAÇÃO FINAL: {}".format(cobra_comp - 1), preto, 30, 60, 80)

            #botao de continuar o jogo
            pygame.draw.rect(fundo, preto, [45,120, 135, 27] )
            texto('Continuar (C)', branco,30, 50, 125)

            #Botao de finalizar o jogo
            pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
            texto('Sair (s)', branco, 30, 195, 125)

            pygame.display.update()  # update para mostrar o ocorrido acima

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sair = False

            # eventos de movimentação
            # and -> evita mover em direções opostas
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    fim_de_jogo = True

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

        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randrange(0, (largura - tamanho), 10)
            maca_y = randrange(0, (altura - tamanho - placar), 10)
            cobra_comp += 1

        if pos_x + tamanho > largura:
            pos_x = 0
        if pos_x < 0:
            pos_x = largura - tamanho  # inicia do outro lado

        if pos_y + tamanho > altura - placar:
            pos_y = 0
        if pos_y < 0:
            pos_y = altura - tamanho - placar

        cobra_inicio = []
        cobra_inicio.append(pos_x)
        cobra_inicio.append(pos_y)
        cobra_XY.append(cobra_inicio)

        if len(cobra_XY) > cobra_comp:
            del cobra_XY[0]
        if any(bloco == cobra_inicio for bloco in cobra_XY[:-1]):
            fim_de_jogo = True

        pygame.draw.rect(fundo, preto, [0, altura - placar, largura, placar])
        texto("Pontuação: {}".format(cobra_comp - 1), branco, 20, 10, altura - 30)

        cobra(cobra_XY)

        maca(maca_x, maca_y)

        relogio.tick(15)
        pygame.display.update()

    pygame.display.update()


jogo()
