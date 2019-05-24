import pygame

# definição de cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# CONTROLE DE FRAMES
controle_FPS = pygame.time.Clock()

# definição do tamanho da tela
LARGURA = 500
ALTURA = 480

# define a altura maxima do pulo
ALTURA_MAXIMA_PULO = 8

# VELOCIDADE DO JOGO
VELOCIDADE_JOGO = 5

# TAMANHO_PERSONAGEM
TAMANHO_PERSONAGEM = 10

# UTILIZADAS NO MOVIMENTO
direita = False
esquerda = False
transicao_de_imagem = 0

imgs_andar_direita = [pygame.image.load('GameImages/R{}.png'.format(i)) for i in range(1, 10)]
imgs_andar_esquerda = [pygame.image.load('GameImages/L{}.png'.format(i)) for i in range(1, 10)]
img_personagem = pygame.image.load('GameImages/standing.png')
background = pygame.image.load('GameImages/bg.jpg')

try:
    pygame.init()
except:
    print("Algo inesperado ocorreu ao iniciar o pygame.")

# inicializa a posicao do personagem
pos_x = 64
pos_y = 280

is_pulando = False
sair_jogo = False

altura_pulo_atual = ALTURA_MAXIMA_PULO

tela = pygame.display.set_mode([LARGURA, ALTURA])
pygame.display.set_caption("Jump Logic")


def redesenhar_tela(pos_x, pos_y):
    global transicao_de_imagem

    controle_FPS.tick(27)
    tela.blit(background, (0, 0))

    # CONFIGURA AS IMAGENS A SEREM CARREGADAS AO ANDAR EM CADA DIREÇÃO
    # faz voltar a lista para o inicio
    print(transicao_de_imagem)
    if transicao_de_imagem + 1 == 27:
        transicao_de_imagem = 0

    if direita:
        tela.blit(imgs_andar_direita[transicao_de_imagem // 3], (pos_x, pos_y))
        transicao_de_imagem += 1

    elif esquerda:
        tela.blit(imgs_andar_esquerda[transicao_de_imagem // 3], (pos_x, pos_y))
        transicao_de_imagem += 1

    else:
        tela.blit(img_personagem, (pos_x, pos_y))
        transicao_de_imagem = 0

    pygame.display.update()


while not sair_jogo:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair_jogo = True

    key_press = pygame.key.get_pressed()

    if key_press[pygame.K_RIGHT]:
        pos_x += VELOCIDADE_JOGO
        direita = True
        esquerda = False

    elif key_press[pygame.K_LEFT]:
        pos_x -= VELOCIDADE_JOGO
        direita = False
        esquerda = True
    else:
        direita = False
        esquerda = False
        transicao_de_imagem = 0

    if key_press[pygame.K_SPACE]:
        is_pulando = True

    if is_pulando:
        if altura_pulo_atual >= -ALTURA_MAXIMA_PULO:
            fl_caindo = 1

            if altura_pulo_atual < 0:  # inversao para o personagem cair
                fl_caindo = -1

            pos_y -= (altura_pulo_atual ** 2) / 2 * fl_caindo
            altura_pulo_atual -= 1
        else:
            altura_pulo_atual = ALTURA_MAXIMA_PULO
            is_pulando = False

    redesenhar_tela(pos_x, pos_y)

pygame.quit()
