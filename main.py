# 
import pygame
import Constantes
from Personaje import personaje

# Variables
Jugador = personaje(50,50)

# Inicialisamos la libreria
pygame.init()

# ventana del juego
ventana = pygame.display.set_mode((1360,768))

# Nombre de la ventana
pygame.display.set_caption("Juego Progra. Avanzada")

# ciclo para mantener ventana
run = True
while run:

    # for para ver los eventos del jquery
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()