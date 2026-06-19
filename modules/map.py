import pytmx
import pygame
import os
from .settings import screen

class Map:
    def __init__(self, name):
        path = os.path.join(__file__,"..", "..", "tilemap", name)
        path = os.path.abspath(path)
        self.TILE_MAP = pytmx.load_pygame(path)
        self.WIDTH = self.TILE_MAP.tilewidth
        self.HEIGHT = self.TILE_MAP.tileheight
        self.collision()
    def show_map(self):
        for layer in self.TILE_MAP.visible_layers:
            if layer.name != "collision":
                for x, y, tile in layer:
                    if tile != 0:
                        image = self.TILE_MAP.get_tile_image_by_gid(tile)
                        screen.blit(image,(x * self.WIDTH, y * self.HEIGHT))
    def collision(self):
        self.LIST_COLLISION = []
        layer_collision = self.TILE_MAP.get_layer_by_name("collision")
        for collision in layer_collision:
            rect = pygame.Rect(collision.x, collision.y, collision.width, collision.height)
            self.LIST_COLLISION.append(rect)
map = Map("tilemap.tmx")