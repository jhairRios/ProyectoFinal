import constantes
import pygame

class Mundo():
    def __init__(self):
        self.tiles_mapa = []

    def procesar_mapa(self, data, lista_tiles):
        self.largo_de_nivel = len(data)

        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                imagen = lista_tiles[tile]
                imagen_rect = imagen.get_rect()
                imagen_x = x * constantes.ESCALA_TILE
                imagen_y = y * constantes.ESCALA_TILE
                imagen_rect.center = (imagen_x, imagen_y)
                tile_data = [imagen, imagen_rect, imagen_x, imagen_y]
                self.tiles_mapa.append(tile_data)

    def dibujar(self, ventana):
        for tile in self.tiles_mapa:
            ventana.blit(tile[0], tile[1])