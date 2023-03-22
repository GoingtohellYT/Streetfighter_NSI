import pygame
from animation import Animation


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
        self.animation = Animation(nb)
        self.image = self.animation.get_current_image()
        self.rect = self.animation.get_current_image().get_rect()
        # On définit la position verticale du joueur à l'écran
        self.rect.y = 500
        self.default_y = 500
        # On définit les paramètres qui varient entre le joueur 1 et le joueur 2
        if nb == 1:
            self.default_x = 260
            self.rect.x = 260
            self.opposite_gr = self.game.player_two_gr
        elif nb == 2:
            self.default_x = 800
            self.rect.x = 800
            self.opposite_gr = self.game.player_one_gr
        self.nb = nb  # On se permet d'utiliser notre numéro de joueur dans les autres fonctions de la classe

    def damage(self, amount):
        # si les deux joueurs sont en collision
        if self.game.check_collision(self, self.opposite_gr):  # si le joueur peut encaisser le coup
            if self.health - amount > 0:
                self.health -= amount
                # On fait reculer le joueur qui quand il reçoit des dégâts → évite le spamming
                if self.game.change_directions() == "1-2" and amount == self.attack:
                    if self.nb == 1 and self.rect.x >= 50:
                        self.rect.x -= 50
                    elif self.nb == 2 and self.rect.x <= 980:
                        self.rect.x += 50
                elif self.game.change_directions() == "2-1" and amount == self.attack:
                    if self.nb == 1 and self.rect.x <= 980:
                        self.rect.x += 50
                    elif self.nb == 2 and self.rect.x >= 50:
                        self.rect.x -= 50
            elif self.health - amount <= 0:  # si le coup est fatal pour le joueur
                self.health = 0
                self.game.game_over()
    
    def update(self, fallFactor):
        if self.jump > 0:
            self.rect.y = self.rect.y - self.jump
            self.jump -= 1
            self.yVelocity = 0
        elif self.rect.y < self.default_y:
            self.rect.y = self.rect.y+(self.yVelocity*fallFactor)  # Faire tomber le joueur
            self.yVelocity += 1
        if self.rect.y > self.default_y:
            self.rect.y = self.default_y

        # Si le joueur souhaite se déplacer...
        if self.animation.state == 1:
            if self.animation.left_direction:  # ... à gauche
                if not self.game.check_collision(self, self.opposite_gr) or self.game.check_positions(self.nb, "left"):  # On vérifie qu'il puisse le faire
                    self.rect.x -= self.runVelocity
            elif not self.animation.left_direction:  # ... à droite
                if not self.game.check_collision(self, self.opposite_gr) or self.game.check_positions(self.nb, "right"):  # On vérifie qu'il puisse le faire
                    self.rect.x += self.runVelocity

        self.animation.update()

    def increased_fall(self):
        if self.rect.y < 350:
            self.update(2)
        if self.game.check_collision(self, self.opposite_gr) and self.rect.y < self.default_y:
            if self.nb == 1:
                self.game.fall_attack(pygame.K_s)
            elif self.nb == 2:
                self.game.fall_attack(pygame.K_DOWN)

    def update_health_bar(self, surface):
        # dessiner la barre de vie du joueur et son arrière-plan
        green = pygame.Color(111, 210, 46)
        red = pygame.Color(217, 0, 0)
        mixture = red.lerp(green, self.health / self.max_health)  # Mélange de couleurs pour la barre de vie
        if self.nb == 1:
            pygame.draw.rect(surface, (60, 63, 60), [20, 20, self.max_health * 4.2, 15])
            pygame.draw.rect(surface, mixture, [20, 20, self.health * 4.2, 15])
        elif self.nb == 2:
            pygame.draw.rect(surface, (60, 63, 60), [640, 20, self.max_health * 4.2, 15])
            pygame.draw.rect(surface, mixture, [640, 20, self.health * 4.2, 15])

    def reset(self):
        self.health = self.max_health
        if self.nb == 1:
            self.rect.x = self.default_x
        elif self.nb == 2:
            self.rect.x = self.default_x
        self.rect.y = self.default_y
