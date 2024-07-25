import pygame

class Weapon():
    def __init__(self,image):
        self.image_original = image
        self.angulo = 0
        self.image = pygame.transform.rotate(self.image_original, self.angulo)
        self.forma = self.image.get_rect()
        
        
    def update(self,personaje):
        self.forma.center = personaje.forma.center
        
    def dibujar(self,interfaz):
        interfaz.blit(self.image, self.forma)
        