import pygame
import math
import constantes

class Arma():

    def __init__(self, image,imagen_bala):
        self.imagen_bala = imagen_bala
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()

    def actualizar(self, personaje):
        bala=None
        self.forma.center = personaje.forma.center
        if personaje.flip == False:
            self.forma.x += personaje.forma.width/10
            self.rotar_arma(False)
        
        elif personaje.flip == True:
            self.forma.x -= personaje.forma.width/10
            self.rotar_arma(True)

        self.forma.y += 10

        #rotar arma con el mouse
        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))

        #click mause
        if pygame.mouse.get_pressed()[0]:
            bala = balas(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
        return bala
        

    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.imagen_original, True, False)

            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original, False, False)

            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

    def dibujar(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen, self.forma)
        pygame.draw.rect(interfaz, constantes.COLOR_ARMA, self.forma, width=1)

class balas(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angulo):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_original = image
        self.angulo = angulo
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.rect = self.imagen.get_rect()
        self.rect.centerx = (x,y)