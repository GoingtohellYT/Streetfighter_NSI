import pygame
from player import Player


# classe qui représente le jeu
class Game:

    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group() # groupe de sprites qui contient les joueurs
        self.player = Player(self) # crée une instance de la classe joueur pour notre joueur
        self.all_players.add(self.player) # on ajoute notre joueur au groupe de sprites
        self.pressed = {}

    def start(self):
        self.is_playing = True
        print("Lancement du jeu")

    def game_over(self):
        self.is_playing = False
        print("Arrêt du jeu")

    def update(self, screen):
        # afficher le joueur
        screen.blit(self.player.image, self.player.rect)
        self.player.update()

        # vérifier si le joueur souhaite et peut se déplacer
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.width + self.player.rect.x < screen.get_width():
            self.player.animation.state = 1
            self.player.animation.left_direction = False
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.animation.state = 1
            self.player.animation.left_direction = True
        else:
            self.player.animation.state = 0
