import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, game, player):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width / 2
        self.rect.y = player.rect.y + player.rect.height / 2
        if player.animation.left_direction:
            self.vx = -8
            self.image = pygame.transform.rotate(self.image, 180)
        else:
            self.vx = 8
        self.vy = 0
        self.owner = player.nb

    def remove(self):
        self.game.projectiles.remove(self)

    def move(self):
        if self.owner == 1 and not self.game.check_collision(self, self.game.player_two_gr):
            self.rect.x = self.rect.x+self.vx
            self.rect.y = self.rect.y+self.vy
        elif self.owner == 1 and self.game.check_collision(self, self.game.player_two_gr):
            self.remove()
            self.game.player_two.damage(self.game.player_one.attack / 2)

        if self.owner == 2 and not self.game.check_collision(self, self.game.player_one_gr):
            self.rect.x = self.rect.x + self.vx
            self.rect.y = self.rect.y + self.vy
        elif self.owner == 2 and self.game.check_collision(self, self.game.player_one_gr):
            self.remove()
            self.game.player_one.damage(self.game.player_two.attack / 2)

        if self.rect.x < 0 or self.rect.x > 1080:
            self.remove()
