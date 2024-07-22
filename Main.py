"""libreria"""
import pygame
import Constantes
from Personaje import personaje


"""Variables"""
Jugador = personaje(50,50)

"""Inicialisamos la libreria"""
pygame.init()

"""ventana del juego"""
ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA,Constantes.ALTO_VENTANA))

"""Nombre de la ventana"""
pygame.display.set_caption("Proyecto clase")

"""Variables de movimiento"""
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

"""ciclo para mantener ventana"""
rum = True
while rum:
    """calcular movimiento del jugador"""
    delta_x = 0
    delta_y = 0
    
    """ciclo de movimiento del jugador"""
    if mover_derecha == True:
        delta_x = 5
    if mover_izquierda == True:
        delta_x = -5
    if mover_arriba == True:
        delta_y = -5
    if mover_abajo == True:
        delta_y = 5
    
    """Mostrar movimiento del personaje"""
    Jugador.movimiento(delta_x,delta_y)
        
    """llamamos a la funcion dbujar jugador"""
    Jugador.dibujar(ventana)

    """for para ver los eventos del jquery"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rum = False
            
        """movimiento del personaje"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event .key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_RIGHT or event .key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_UP or event .key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_DOWN or event .key == pygame.K_s:
                mover_abajo = True
            
    """Actualizar la pantalla del juego"""
    pygame.display.update()
    
    """fin del juego"""
pygame.quit()