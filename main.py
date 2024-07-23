import pygame
import constantes
from personaje import Personaje

# Inicialisamos la libreria
pygame.init()

# ventana del juego
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

# Nombre de la ventana
pygame.display.set_caption("Juego Progra. Avanzada")

# Variables
jugador = Personaje(50,50)

#definir variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

# controlar el movimiento del jugador
reloj = pygame.time.Clock()


# ciclo para mantener ventana
run = True
while run:

    # velocidad de 60 fps
    reloj.tick(constantes.FPS)
    
    ventana.fill(constantes.COLOR_BG)

    # calcular movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD_PERSONAJE

    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD_PERSONAJE

    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD_PERSONAJE

    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD_PERSONAJE

    # mover al jugar
    jugador.movimiento(delta_x, delta_y)

    jugador.dibujar(ventana)

    # for para ver los eventos del jquery
    for event in pygame.event.get():

        #evento para cerra la ventana
        if event.type == pygame.QUIT:
            run = False

        # evento para mover el personaje
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_a or event.key == pygame.K_LEFT:
                mover_izquierda = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                mover_derecha = True
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                mover_arriba = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                mover_abajo = True

        # evento para dejar de mover el personaje
        if event.type == pygame.KEYUP:
            if event.key ==  pygame.K_a or event.key == pygame.K_LEFT:
                mover_izquierda = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                mover_derecha = False
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                mover_arriba = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                mover_abajo = False

    pygame.display.update()

pygame.quit()