import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animaciones, energia):
        self.llave = 0
        self.energia = energia
        self.vivo = True
        self.flip = False
        self.animaciones = animaciones
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.forma = self.image.get_rect()
        self.forma.center = (x, y)
        self.en_movimiento = False  # Bandera para controlar el movimiento
        

    def actualizar(self):
        # comprobar si el jugador esta muerto
        if self.energia <= 0:
            self.energia = 0
            self.vivo = False

        cooldown_animacion = constantes.COOLDOWN_ANIMACION
        if self.en_movimiento:
            if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
                self.frame_index = (self.frame_index + 1) % len(self.animaciones)
                self.update_time = pygame.time.get_ticks()
        self.image = self.animaciones[self.frame_index]

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        #pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma, width=1)

    def movimiento(self, delta_x, delta_y):
        posicion_pantalla = [0, 0]

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

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

        
        if self.forma.right > (constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA_R):
            posicion_pantalla[0] = (constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA_R) - self.forma.right
            self.forma.right = constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA_R
        if self.forma.left < constantes.LIMITE_PANTALLA_L:
            posicion_pantalla[0] = constantes.LIMITE_PANTALLA_L - self.forma.left
            self.forma.left = constantes.LIMITE_PANTALLA_L

        if self.forma.bottom > (constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA_B):
            posicion_pantalla[1] = (constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA_B) - self.forma.bottom
            self.forma.bottom = constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA_B
        if self.forma.top < constantes.LIMITE_PANTALLA_T:
            posicion_pantalla[1] = constantes.LIMITE_PANTALLA_T - self.forma.top
            self.forma.top = constantes.LIMITE_PANTALLA_T
            
        return posicion_pantalla

class Enemigos():
    def __init__(self, x, y, animaciones, energia):
        self.energia = energia
        self.vivo = True
        self.flip = False
        self.animaciones = animaciones
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.forma = self.image.get_rect()
        self.forma.center = (x, y)

    def actualizar(self):
        # comprobar si el enemigo esta muerto
        if self.energia <= 0:
            self.energia = 0
            self.vivo = False

        cooldown_animacion = constantes.COOLDOWN_ANIMACION
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = (self.frame_index + 1) % len(self.animaciones)
            self.update_time = pygame.time.get_ticks()
        self.image = self.animaciones[self.frame_index]

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)