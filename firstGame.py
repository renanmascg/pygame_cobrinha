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
altura = 240
tamanho = 10  # pixels

# configuração da janela do jogo
relogio = pygame.time.Clock()  # limitar a quantidade de frames por segundos
fundo = pygame.display.set_mode(size=(largura, altura))
pygame.display.set_caption("Snake")
font = pygame.font.SysFont(None, 15)


def texto(msg, cor):
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [largura / 10, altura / 2])


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
    maca_y = randrange(0, (altura - tamanho), 10)

    velocidade_x = 0
    velocidade_y = 0

    cobra_XY = []
    cobra_comp = 1

    while sair:

        while fim_de_jogo:
            fundo.fill(branco)
            texto("Fim de Jogo, para continuar tecle C ou S para sair", vermelho)
            pygame.display.update()  # update para mostrar o ocorrido acima
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

        cobra_inicio = []
        cobra_inicio.append(pos_x)
        cobra_inicio.append(pos_y)
        cobra_XY.append(cobra_inicio)

        if len(cobra_XY) > cobra_comp:
            del cobra_XY[0]
        if any(bloco == cobra_inicio for bloco in cobra_XY[:-1]):
            # if cobra_inicio in cobra_XY[:-1]:
            fim_de_jogo = True

        cobra(cobra_XY)
        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randrange(0, (largura - tamanho), 10)
            maca_y = randrange(0, (altura - tamanho), 10)
            cobra_comp += 1

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
