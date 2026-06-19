import pygame
import os
from .settings import screen

class Sprite:
    def __init__(self, width: int, height: int, image_name: str, x: int, y: int):
        self.WIDTH = width
        self.HEIGTH = height
        self.IMAGE_NAME = image_name     
        self.X = x
        self.Y = y
        self.img_load()
    def img_load(self):
        path = os.path.join(__file__, "..", "..", "images", self.IMAGE_NAME)
        path = os.path.abspath(path)
        image = pygame.image.load(path)
        self.IMAGE = pygame.transform.scale(image,(self.WIDTH, self.HEIGTH))
    def show_image(self):
        screen.blit(self.IMAGE, (self.X, self.Y))
object = Sprite(width = 1500, height = 700, image_name = "bg.png", x = 0, y = 0)