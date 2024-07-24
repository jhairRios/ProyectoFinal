import pygame
import Constantes

class personaje():
    #tamano del personaje
    def __init__(self,x,y,animaciones):
        #voltear el personaje
        self.flip = False
        #hacer que el personaje se mueva
        self.animaciones = animaciones
        #imagen animacion
        self.freame_index = 0
        #alcacenamiento del tiempo de pygame
        self.update_time = pygame.time.get_ticks()
        #llamar la imagen
        self.image = animaciones[self.freame_index] 
        #tamaño del personaje
        self.forma = pygame.Rect(0, 0, Constantes.ANCHO_PERSONAJE,
                                       Constantes.ALTO_PERSONAJE)
        self.forma.center = (x,y)
        
    #Movimiento del personaje
    def movimiento(self, delta_x, delta_y):
        #ciclo invertir personaje
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False
            
        #posicion del personaje
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
        
        #actualizar la imagen
    def update(self):
        cooldown_animacion = 100
        self.image = self.animaciones[self.freame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.freame_index = self.freame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.freame_index >= len(self.animaciones):
            self.freame_index = 0
    #divujar el personaje
    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip,False)
        interfaz.blit(imagen_flip, self.forma)
        #pygame.draw.rect(interfaz,Constantes.COLOR_PERSONAJE , self.forma)