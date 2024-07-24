#libreria
import pygame
import Constantes
from Personaje import personaje

#Inicialisamos la libreria
pygame.init()

#ventana del juego
ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA,Constantes.ALTO_VENTANA))

def escalar_img (image,escala):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image,(int(w*escala),int(h*escala)))
    return nueva_imagen

#animacion del personaje
animaciones = []
#for para cargar las imagenes
for i in range(8):
    img = pygame.image.load(f"Viking pack//Base sprite//caminar_{i}.png")
    img = escalar_img(img,Constantes.ESCALA_PERSONAJE)
    animaciones.append(img)


#Variables
Jugador = personaje(50,50,animaciones)

#Nombre de la ventana
pygame.display.set_caption("Proyecto clase")

#Variables de movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#FRAME DEL JUEGO
reloj = pygame.time.Clock()

#ciclo para mantener ventana
rum = True
while rum:
    
    #FPS
    reloj.tick(Constantes.FPS)
    
    #COLOR DE LA VENTANA
    ventana.fill(Constantes.COLOR_BG)
    
    #calcular movimiento del jugador
    delta_x = 0
    delta_y = 0
    
    #ciclo de movimiento del jugador
    if mover_derecha == True:
        delta_x = Constantes.VELOCIDAD_PERSONAJE
    if mover_izquierda == True:
        delta_x = -Constantes.VELOCIDAD_PERSONAJE
    if mover_arriba == True:
        delta_y = -Constantes.VELOCIDAD_PERSONAJE
    if mover_abajo == True:
        delta_y = Constantes.VELOCIDAD_PERSONAJE
    
    #Mostrar movimiento del personaje
    Jugador.movimiento(delta_x,delta_y)
    
    #actualizar movimiento del personaje
    Jugador.update()
        
    #llamamos a la funcion dbujar jugador
    Jugador.dibujar(ventana)

    #for para ver los eventos del jquery
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rum = False
            
        #movimiento del personaje
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event .key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_RIGHT or event .key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_UP or event .key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_DOWN or event .key == pygame.K_s:
                mover_abajo = True
        #Detener movimineto del personaje
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event .key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_RIGHT or event .key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_UP or event .key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_DOWN or event .key == pygame.K_s:
                mover_abajo = False
            
    #Actualizar la pantalla del juego
    pygame.display.update()
    
    #fin del juego
pygame.quit()