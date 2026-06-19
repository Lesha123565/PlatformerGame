import pygame 
from .image import Sprite
from .settings import screen
from .map import map 
class Hero(Sprite):
    def __init__(self, width, height, image_name, x, y, speed):
        Sprite.__init__(self, width, height, image_name, x, y)
        self.SPEED = speed
    def check_collision(self):
        self.RECT_HERO = pygame.Rect(self.X + 15, self.Y +15, self.WIDTH - 30, self.HEIGTH - 15)
        pygame.draw.rect(screen, "red", self.RECT_HERO)
        self.CAN_MOVE_RIGHT = True
        self.CAN_MOVE_LEFT = True
        self.CAN_MOVE_DOWN = True
        for platform in map.LIST_COLLISION:
            left_rect = pygame.Rect(platform.x, platform.y, 2 , platform.height)
            pygame.draw.rect(screen, "blue", left_rect)
            top_rect= pygame.Rect(platform.x,platform.y,platform.width, 2)
            pygame.draw.rect(screen, "blue", top_rect)
            bottom_rect= pygame.Rect(platform.x,platform.y + platform.height, platform.width, 4)
            pygame.draw.rect(screen, "blue", bottom_rect)
            right_rect= pygame.Rect(platform.x + platform.width, platform.y, 2, platform.height)
            pygame.draw.rect(screen, "blue", right_rect)
            if self.RECT_HERO.colliderect(left_rect):
                self.CAN_MOVE_RIGHT = False
            if self.RECT_HERO.colliderect(right_rect):
                self.CAN_MOVE_LEFT = False
            if self.RECT_HERO.colliderect(top_rect):
                self.CAN_MOVE_DOWN = False
    def move(self):
        self.check_collision()
        self.LIST_KEYS = pygame.key.get_pressed()
        if self.LIST_KEYS[pygame.K_d] and self.CAN_MOVE_RIGHT:
            self.X += self.SPEED
        if self.LIST_KEYS[pygame.K_a] and self.CAN_MOVE_LEFT:
            self.X -= self.SPEED
        if self.CAN_MOVE_DOWN:
            self.Y += self.SPEED

hero = Hero(width=80, height=80, image_name="hero.png", x= 100, y= 100, speed= 7)