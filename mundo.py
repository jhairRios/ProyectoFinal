import constantes
import pygame

class Mundo():
    def __init__(self):
        self.tiles_mapa = []

    def procesar_mapa(self, data, lista_tiles):
        self.largo_de_nivel = len(data[0])

        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                imagen = lista_tiles[tile]
                imagen_rect = imagen.get_rect()
                imagen_x = x * constantes.ESCALA_TILE
                imagen_y = y * constantes.ESCALA_TILE
                imagen_rect.center = (imagen_x, imagen_y)
                tile_data = [imagen, imagen_rect, imagen_x, imagen_y]
                self.tiles_mapa.append(tile_data)

    def actualizar(self, posicion_pantalla):
        for tile in self.tiles_mapa:
            tile[2] += posicion_pantalla[0]
            tile[3] += posicion_pantalla[1]
            tile[1].center = (tile[2], tile[3])

    def dibujar(self, ventana):
        for tile in self.tiles_mapa:
            ventana.blit(tile[0], tile[1])