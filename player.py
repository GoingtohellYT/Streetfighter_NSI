import pygame
from animation import animation


class Player(pygame.sprite.Sprite):
    def __init__(self, game, nb):
        self.game = game
        super().__init__()
        # On définit les statistiques de base du joueur
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.jump = 0
        self.runVelocity = 5
        self.yVelocity = 0
        # On définit les sprites
        self.animation = animation(nb)
        self.image = self.animation.get_current_image()
        self.rect = self.animation.get_current_image().get_rect()
        # On définit la position verticale du joueur à l'écran
        self.rect.y = 500
        # On définit les paramètres qui varient entre le joueur 1 et le joueur 2
        if nb == 1:
            self.rect.x = 450
            self.opposite_gr = self.game.player_two_gr
        elif nb == 2:
            self.rect.x = 650
            self.opposite_gr = self.game.player_one_gr
        self.nb = nb  # On se permet d'utiliser notre numéro de joueur dans les autres fonctions de la classe
    
    def update(self):
        if self.jump > 0:
            self.rect.y = self.rect.y-self.jump
            self.jump = self.jump-1
            self.yVelocity = 0
        elif self.rect.y < 500:
            self.rect.y = self.rect.y+self.yVelocity  # Faire tomber le joueur
            self.yVelocity += 1

        # Si le joueur souhaite se déplacer...
        if self.animation.state == 1:
            if self.animation.left_direction:  # ... à gauche
                if not self.game.check_collision(self, self.opposite_gr) or self.game.check_positions(self.nb, "left"):  # On vérifie qu'il puisse le faire
                    self.rect.x -= self.runVelocity
            elif not self.animation.left_direction:  # ... à droite
                if not self.game.check_collision(self, self.opposite_gr) or self.game.check_positions(self.nb, "right"):  # On vérifie qu'il puisse le faire
                    self.rect.x += self.runVelocity

        self.animation.update()



