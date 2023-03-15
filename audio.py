import pygame


class SoundManager:
    def __init__(self):
        self.sounds = {
            "attack1": pygame.mixer.Sound("assets/sounds/OOT_AdultLink_StrongAttack1.wav"),
            "attack2": pygame.mixer.Sound("assets/sounds/OOT_AdultLink_StrongAttack2.wav"),
            "fight": pygame.mixer.Sound("assets/sounds/Street_Fighter_Fight.mp3"),
            "game_over": pygame.mixer.Sound("assets/sounds/Game_Over.mp3"),
            "p1_victory": pygame.mixer.Sound("assets/sounds/Player_1_Wins.mp3"),
            "p2_victory": pygame.mixer.Sound("assets/sounds/Player_2_Wins.mp3")
        }

    def play(self, name):
        self.sounds[name].play()
