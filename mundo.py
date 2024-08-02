import constantes
from items import Item

paredes = [0, 1, 2, 6, 8, 9, 11, 13, 18, 30, 37]

class Mundo():
    def __init__(self):
        self.tiles_mapa = []
        self.tile_paredes = []
        self.tile_salida = None
        #self.tile_llave = 0
        self.lista_item = []

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
                 #agregar tiles a la lista de paredes
                
                # if tile in paredes:
                #     self.tile_paredes.append(tile_data)
                # elif tile == 18: # and tile == 1:
                #     self.tile_salida = tile_data
                # elif tile == 30:
                #     llave = Item(imagen_x, imagen_y, 0, item_imagenes[0])
                #     self.lista_item.append(llave)
                #     tile_data[0] = lista_tiles[38]
                # elif tile == 37:
                #     botiquin = Item(imagen_x, imagen_y, 1, item_imagenes[1])
                #     self.lista_item.append(botiquin)
                #     tile_data[0] = lista_tiles[38]

                self.tiles_mapa.append(tile_data)

    def actualizar(self, posicion_pantalla):
        for tile in self.tiles_mapa:
            tile[2] += posicion_pantalla[0]
            tile[3] += posicion_pantalla[1]
            tile[1].center = (tile[2], tile[3])

    def dibujar(self, ventana):
        for tile in self.tiles_mapa:
            ventana.blit(tile[0], tile[1])