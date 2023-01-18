import pygame
from Spritesheet import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.spritesheet = SpriteSheet("assets/player1_idle.png")
        self.image = self.spritesheet.image_at((0,0,32,64))
        self.image_index = 0
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    def animate(self):
        self.image_index += 1
        if self.image_index == 6:
            self.image_index = 0

        self.image = self.spritesheet.image_at((self.image_index*32,0,32,64))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
