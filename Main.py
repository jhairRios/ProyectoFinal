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

"""ciclo para mantener ventana"""
rum = True
while rum:

    """for para ver los eventos del jquery"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rum = False
pygame.quit()