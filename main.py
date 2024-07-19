import pygame

ancho = 1366
alto = 768

ventana = pygame.display.set_mode((ancho, alto))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()