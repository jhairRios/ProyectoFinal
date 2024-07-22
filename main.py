import pygame
import constantes
from personaje import Personaje

# Variables
jugador = Personaje(50,50)

# Inicialisamos la libreria
pygame.init()

# ventana del juego
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

# Nombre de la ventana
pygame.display.set_caption("Juego Progra. Avanzada")

#definir variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

# ciclo para mantener ventana
run = True
while run:

    # calcular movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = 5

    if mover_izquierda == True:
        delta_x = -5

    if mover_arriba == True:
        delta_y = -5

    if mover_abajo == True:
        delta_y = 5

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
            if event.key ==  pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True


    pygame.display.update()

pygame.quit()