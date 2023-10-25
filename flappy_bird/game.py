import random
import sys

import pygame

import consts

from plane import Plane
from ground import Ground
from pipe import Pipe

class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
        pygame.display.set_caption(consts.TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        # Inicialização de grupos de sprites
        self.all_sprites = pygame.sprite.Group()
        self.plane = Plane() # isso aqui é criar um construtor?
        self.ground = Ground()
        self.all_sprites.add(self.plane, self.ground)
        self.pipes = pygame.sprite.Group()

        self.score = 0

    def game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT    :
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.plane.flap()

    def run(self):
        while self.running:
            self.clock.tick(consts.FPS)
            self.game_events()

            self.all_sprites.draw(self.screen)

            if len(self.pipes) < 2:
                self.spawn_pipe()
            self.remove_pipes()

            hits = pygame.sprite.spritecollide(self.plane, [self.ground], False)
            if hits:
                self.running = False

            hits = pygame.sprite.spritecollide(self.plane, self.pipes, False)
            if hits:
                self.running = False

            self.font = pygame.font.Font(None, 36)
            self.score_text = self.font.render(f"Score: {self.score}", True, consts.WHITE)
            self.screen.blit(self.score_text, (10, 10))

            self.all_sprites.update()
            pygame.display.flip()

            self.screen.fill(consts.BLACK)
        
        pygame.quit()
        sys.exit()

    def randomize_height(self):
        self.y = random.randint(100, 500)

    def spawn_pipe(self):
        self.randomize_height()
        self.pipe_bot = Pipe(300, self.y, "sprites/pipe.png")
        self.pipe_top = Pipe(300, (self.y - consts.PIPE_GAP - 500), "sprites/pipe_top.png")

        self.pipes.add(self.pipe_bot, self.pipe_top)
        self.all_sprites.add(self.pipe_bot, self.pipe_top)

    def remove_pipes(self):
        for pipe in self.pipes:
            if pipe.rect.x < 0:
                self.pipes.remove(pipe)
                self.all_sprites.remove(pipe)
                self.score += 1
