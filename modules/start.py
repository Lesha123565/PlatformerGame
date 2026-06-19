import pygame
from .settings import screen
from .image import object
from .map import map
from .hero import hero

def start():
    run = True
    while run:
        events = pygame.event.get()
        # object.X += 3
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        screen.fill((255, 255, 255))
        object.show_image()
        map.show_map()
        hero.show_image()
        for rect in map.LIST_COLLISION:
            pygame.draw.rect(screen, "green", rect)
        hero.move()
        pygame.display.flip()

