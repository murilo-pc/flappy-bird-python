import pygame
import random
pygame.init()

tela = pygame.display.set_mode((500, 500))
velocidade = 0 #pixels / segundo
y = 100
canox = 500
canoy = 250
pontos = 0
rodando = True
time = pygame.time.Clock()

point = pygame.mixer.Sound("assets/point.wav")
jump = pygame.mixer.Sound("assets/jump.wav")
fonte = pygame.font.SysFont("Arial", 32, bold=True)
cano = pygame.transform.scale(pygame.image.load("assets/cano.png").convert_alpha(), (50, 450))
fundo = pygame.transform.scale(pygame.image.load("assets/fundo.png").convert_alpha(), (500,500))
img_player = pygame.transform.scale(pygame.image.load("assets/bird.png").convert_alpha(), (50, 50)) 

while rodando:
    pontos_text = fonte.render(f"score: {pontos}", True, (0, 0 , 0))
    img_player_rotate = pygame.transform.rotate(img_player, velocidade/275*45*-1)
    #multiplique x por delta para fazer andar x pixels por segundo
    delta = time.tick(60) / 1000
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                velocidade = -275
                jump.play()
    if canox < -50:
        canox = 500
        canoy = random.randint(100, 400)
        pontos += 1
        point.play()

    
    velocidade += 400 * delta
    y += velocidade * delta
    canox -= 250 * delta
    
    tela.blit(fundo, (0, 0))
    tela.blit(cano, (canox, canoy + 75))
    tela.blit(pygame.transform.rotate(cano, 180), (canox, canoy - 525)) 
    tela.blit(img_player_rotate, (100, y)) 
    tela.blit(pontos_text, (10, 10))  

    pygame.display.flip()

    if y >= 450 or (canox > 50 and canox < 150 and ((y < canoy - 75) or (y > canoy + 25 ))) or y <= -50: 
        rodando = False