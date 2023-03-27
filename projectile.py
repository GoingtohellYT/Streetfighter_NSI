import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, game, player):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.rect = self.game.bullet_image.get_rect()
        self.rect.x = player.rect.x + player.rect.width / 2
        self.rect.y = player.rect.y + player.rect.height / 2
        if player.animation.left_direction:
            self.vx = -8
        else:
            self.vx = 8
        self.vy = 0
        self.owner = player.nb

    def remove(self, ):
        self.game.projectiles.remove(self)

    def move(self, ):
        self.rect.x = self.rect.x+self.vx
        self.rect.y = self.rect.y+self.vy

        if self.rect.x < 0 or self.rect.x > 1080:
            self.remove()
