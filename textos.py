import pygame
import constantes

class Texto_de_danio(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, font, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(str(damage), True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.contador = 0

    def update(self, posicion_pantalla):
        # reposicionar basado en la posicion de la pantalla
        self.rect.x += posicion_pantalla[0]
        self.rect.y += posicion_pantalla[1]

        self.rect.y -= 2
        self.contador += 1
        if self.contador > 30:
            self.kill()