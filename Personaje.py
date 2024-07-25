import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)
        self.en_movimiento = False  # Bandera para controlar el movimiento

    def actualizar(self):
        cooldown_animacion = 100
        if self.en_movimiento:
            if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
                self.frame_index = (self.frame_index + 1) % len(self.animaciones)
                self.update_time = pygame.time.get_ticks()
        self.image = self.animaciones[self.frame_index]

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)

    def movimiento(self, delta_x, delta_y):
        if delta_x != 0 or delta_y != 0:
            self.en_movimiento = True
        else:
            self.en_movimiento = False
            self.frame_index = 0  # Restablecer al primer fotograma

        # Actualiza la dirección del personaje
        if delta_x > 0:
            self.flip = False
        elif delta_x < 0:
            self.flip = True

        self.forma.x += delta_x
        self.forma.y += delta_y