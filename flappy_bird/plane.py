import pygame
import consts

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("sprites/plane.png")

        self.rect = self.image.get_rect()
        self.rect.center = (100, consts.SCREEN_HEIGHT//2)
        self.velocity = 0

    def update(self):
        self.velocity += consts.GRAVITY
        self.rect.y += self.velocity
    
    def flap(self):
        self.velocity = -consts.FLAP_STRENGTH