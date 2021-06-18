import pygame
import sys

#inicialização
pygame.init()
clock = pygame.time.Clock()

#configurando uma janela
screen = pygame.display.set_mode((960, 640))
pygame.display.set_caption('Pong')

#obejetos
ball = pygame.Rect(960/2-15, 640/2-15, 30, 30)
player = pygame.Rect(960-20, 640/2-70, 10, 140)
opponent = pygame.Rect(10,640/2-70, 10, 140)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Desenho
    pygame.draw.rect(screen, (200, 200, 200), ball)
    pygame.draw.rect(screen, (200, 200, 200), player)
    pygame.draw.rect(screen, (200, 200, 200), opponent)

    #Atualizando a janela 60fps
    pygame.display.flip()
    clock.tick(60)
