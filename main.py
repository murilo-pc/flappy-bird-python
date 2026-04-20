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
while rodando:
    #multiplique x por delta para fazer andar x pixels por segundo
    delta = time.tick(60) / 1000
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                velocidade = -250
    if canox < -50:
        canox = 500
        canoy = random.randint(100, 400)

    tela.fill((200, 200, 255))
    velocidade += 350 * delta
    y += velocidade * delta
    canox -= 250 * delta

    pygame.draw.rect(tela, (0, 255, 0), (canox, canoy - 525, 50, 450))
    pygame.draw.rect(tela, (0, 255, 0), (canox, canoy + 75, 50, 450))
    pygame.draw.rect(tela, (255, 255, 0), (100, y, 50, 50)) 


    pygame.display.flip()

    if y >= 450 or (canox > 50 and canox < 150 and ((y < canoy - 75) or (y > canoy + 25 ))) : 
        rodando = False
