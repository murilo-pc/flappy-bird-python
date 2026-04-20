import pygame
import random
pygame.init()

tela = pygame.display.set_mode((500, 500))
velocidade = 0 #pixels / segundo
y = 100
canox = 500
canoy = 250

rodando = True
time = pygame.time.Clock()

cano = pygame.transform.scale(pygame.image.load("assets/cano.png").convert_alpha(), (50, 450))
fundo = pygame.transform.scale(pygame.image.load("assets/fundo.png").convert_alpha(), (500,500))
img_player = pygame.transform.scale(pygame.image.load("assets/bird.png").convert_alpha(), (50, 50)) 

while rodando:
    img_player_rotate = pygame.transform.rotate(img_player, velocidade/275*45*-1)
    #multiplique x por delta para fazer andar x pixels por segundo
    delta = time.tick(60) / 1000
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                velocidade = -275
    if canox < -50:
        canox = 500
        canoy = random.randint(100, 400)

    tela.blit(fundo, (0, 0))
    velocidade += 400 * delta
    y += velocidade * delta
    canox -= 250 * delta

    
    pygame.draw.rect(tela, (0, 255, 0), (canox, canoy - 525, 50, 450))
    pygame.draw.rect(tela, (0, 255, 0), (canox, canoy + 75, 50, 450))
    tela.blit(img_player_rotate, (100, y)) 


    pygame.display.flip()

    if y >= 450 or (canox > 50 and canox < 150 and ((y < canoy - 75) or (y > canoy + 25 ))) : 
        rodando = False
