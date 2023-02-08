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
        self.jump = 0
        self.runVelocity = 5
        self.yVelocity = 0;
        self.animation = animation()
        self.rect = self.animation.get_current_image().get_rect()
        self.rect.x = 450
        self.rect.y = 500
    
    def update(self):
        if self.jump>0:
            self.rect.y=self.rect.y-self.jump
            self.jump=self.jump-1
        if self.rect.y<500:
            self.rect.y=self.rect.y+5 #Faire tomber le joueur
        
        if self.animation.state == 1:
            if self.animation.left_direction:
                self.rect.x -= self.runVelocity
            else:
                self.rect.x += self.runVelocity

        self.animation.update()
        if self.runVelocity!=0:
            self.animation.state = 1
        else:
            self.animation.state = 0
