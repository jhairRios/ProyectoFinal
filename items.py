import pygame.sprite
import constantes
from personaje import *

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type, animacion_list):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type # 0 = monedas, 1 = botiquin
        self.animacion_list = animacion_list
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animacion_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, personaje):
        # comprobar colision entre personaje y item
        if self.rect.colliderect(personaje.forma):
            #moneda
            if self.item_type == 0:
                personaje.monedas += 1
            #botiquin
            elif self.item_type == 1:
                personaje.energia += 100
                if personaje.energia > 500:
                    personaje.energia = 500

            self.kill()

        cooldown_animacion = constantes.COOLDOWN_MONEDA
        self.image = self.animacion_list[self.frame_index]

        if pygame.time.get_ticks() - self.update_time > cooldown_animacion:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()

        if self.frame_index >= len(self.animacion_list):
            self.frame_index = 0