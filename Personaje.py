import pygame

class personaje():
    def __init__(self,x,y):
        self.forma = pygame.Rect(0, 0, 20, 20)
        self.forma.center = (x,y)

        def dbujar(self, interfaz):
            pygame.draw.rect(interfaz, (255, 255, 0), self.forma)