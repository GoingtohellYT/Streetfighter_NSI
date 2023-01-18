import pygame
from Spritesheet import SpriteSheet
from animation import animation


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.spritesheet = SpriteSheet("assets/player1_idle.png")
        self.image = self.spritesheet.image_at((0,0,32,64))
        self.image_index = 0
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500
        self.animation = animation()

    def update(self):
        if self.animation.state == 1:
            if self.animation.left_direction:
                self.rect.x -= self.velocity
            else:
                self.rect.x += self.velocity

        self.animation.update()
        if self.velocity!=0:
            self.animation.state = 1
        else:
            self.animation.state = 0
