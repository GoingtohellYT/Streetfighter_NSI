import pygame
from player import Player


# classe qui représente le jeu
class Game:

    def __init__(self):
        self.is_playing = False
        self.player_one_gr = pygame.sprite.Group()  # groupe de sprites qui contient les joueurs
        self.player_two_gr = pygame.sprite.Group()
        self.player_one = Player(self, 1)  # crée une instance de la classe joueur pour notre joueur
        self.player_two = Player(self, 2)  # crée une seconde instance de la classe joueur
        self.player_one_gr.add(self.player_one)  # on ajoute notre joueur au groupe de sprites
        self.player_two_gr.add(self.player_two)
        self.pressed = {}

    def start(self):
        self.is_playing = True
        print("Lancement du jeu")

    def game_over(self):
        self.is_playing = False
        print("Arrêt du jeu")

    # On vérifie si les deux joueurs se touchent
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # On vérifie si le joueur adverse empêche notre joueur de se déplacer et on renvoie True si l'on peut bouger et False si le passage est bloqué
    def check_positions(self, player, direction):
        if direction == "left":
            if player == 1:
                if self.player_one.rect.x < self.player_two.rect.x:
                    return True
                else:
                    return False
            elif player == 2:
                if self.player_two.rect.x < self.player_one.rect.x:
                    return True
                else:
                    return False
        elif direction == "right":
            if player == 1:
                if self.player_one.rect.x > self.player_two.rect.x:
                    return True
                else:
                    return False
            elif player == 2:
                if self.player_two.rect.x > self.player_one.rect.x:
                    return True
                else:
                    return False

    def update(self, screen):
        # afficher le joueur
        screen.blit(self.player_one.animation.get_current_image(), self.player_one.rect)
        self.player_one.update()
        screen.blit(self.player_two.animation.get_current_image(), self.player_two.rect)
        self.player_two.update()

        # vérifier si le joueur 1 souhaite et peut se déplacer dans les limites de l'écran
        if self.pressed.get(
                pygame.K_RIGHT) and self.player_one.rect.width + self.player_one.rect.x < screen.get_width():
            self.player_one.animation.state = 1
            self.player_one.animation.left_direction = False
        elif self.pressed.get(pygame.K_LEFT) and self.player_one.rect.x > 0:
            self.player_one.animation.state = 1
            self.player_one.animation.left_direction = True
        else:
            self.player_one.animation.state = 0

        if self.pressed.get(pygame.K_UP) and self.player_one.rect.y == 500:
            self.player_one.jump = 20

        # idem pour le joueur 2
        if self.pressed.get(
                pygame.K_d) and self.player_two.rect.width + self.player_two.rect.x < screen.get_width():
            self.player_two.animation.state = 1
            self.player_two.animation.left_direction = False
        elif self.pressed.get(pygame.K_q) and self.player_two.rect.x > 0:
            self.player_two.animation.state = 1
            self.player_two.animation.left_direction = True
        else:
            self.player_two.animation.state = 0

        if self.pressed.get(pygame.K_z) and self.player_two.rect.y == 500:
            self.player_two.jump = 20
