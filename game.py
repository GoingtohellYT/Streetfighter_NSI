import pygame


# classe qui représente le jeu
class Game:

    def __init__(self):
        self.is_playing = False

    def start(self):
        self.is_playing = True
        print("Lancement du jeu")

    def game_over(self):
        self.is_playing = False
        print("Arrêt du jeu")
