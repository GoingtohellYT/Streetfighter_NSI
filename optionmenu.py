import pygame
from keyentry import Keyentry
from animation import Animation
from file_manager import File
class Optionmenu:

    def __init__(self, game):
        self.game = game
        self.isOpened = False

        self.fontTitle = pygame.font.SysFont("Bauhaus 93", 45)
        self.font = pygame.font.SysFont("Bauhaus 93", 25)
        self.smallFont = pygame.font.SysFont("Bauhaus 93", 20)
        self.greyColor = (10,10,10)

        self.player1Entries = list()
        self.player2Entries = list()

        self.file = File(self.game)
        self.file.load()

        self.player1Entries.append(
            Keyentry(self, "Se déplacer vers la gauche : ", game.player_one.keys[0], game.player_one, game, 0))
        self.player1Entries.append(
            Keyentry(self, "Se déplacer vers la droite : ", game.player_one.keys[2], game.player_one, game, 2))
        self.player1Entries.append(Keyentry(self, "Sauter : ", game.player_one.keys[1], game.player_one, game, 1))
        self.player1Entries.append(
            Keyentry(self, "Attaque sautée : ", game.player_one.keys[3], game.player_one, game, 3))
        self.player1Entries.append(Keyentry(self, "Attaque: ", game.player_one.keys[4], game.player_one, game, 4))
        self.player1Entries.append(Keyentry(self, "Tirer : ", game.player_one.keys[5], game.player_one, game, 5))

        self.player2Entries.append(
            Keyentry(self, "Se déplacer vers la gauche : ", game.player_two.keys[0], game.player_two, game, 0))
        self.player2Entries.append(
            Keyentry(self, "Se déplacer vers la droite : ", game.player_two.keys[2], game.player_two, game, 2))
        self.player2Entries.append(Keyentry(self, "Sauter : ", game.player_two.keys[1], game.player_two, game, 1))
        self.player2Entries.append(
            Keyentry(self, "Attaque sautée : ", game.player_two.keys[3], game.player_two, game, 3))
        self.player2Entries.append(Keyentry(self, "Attaque: ", game.player_two.keys[4], game.player_two, game, 4))
        self.player2Entries.append(Keyentry(self, "Tirer : ", game.player_two.keys[5], game.player_two, game, 5))

        self.animationplayer1 = Animation(1) # Ajoute une animation du joueur 1 pour la déco
        self.animationplayer2 = Animation(2)
        self.animationplayer1.resize(120, 240) # Agrandir les images
        self.animationplayer2.resize(120, 240) # Agrandir les images

    def update(self, screen):
        #Dessine un fond un peu transparent pour mieux contraster le texte:
        backgroundGreyImg = pygame.Surface((1080, 650))
        backgroundGreyImg.set_alpha(180)  # Transparence
        backgroundGreyImg.fill(self.greyColor)  # Remplir l'image
        screen.blit(backgroundGreyImg, (0, 70)) # Afficher l'image

        player1TitleText = self.fontTitle.render("Joueur 1", 1, (240, 240, 240))
        screen.blit(player1TitleText, (10, 75))
        player2TitleText = self.fontTitle.render("Joueur 2", 1, (240, 240, 240))
        screen.blit(player2TitleText, (550, 75))
        for i in range(len(self.player1Entries)):
            self.player1Entries[i].update(10, 145+i*40, screen)
        for i in range(len(self.player2Entries)):
            self.player2Entries[i].update(550, 145 + i * 40, screen)

        # Animation Joueur
        self.animationplayer1.update()
        self.animationplayer2.update()
        screen.blit(self.animationplayer1.get_current_image(), (210, 400))
        screen.blit(self.animationplayer2.get_current_image(), (750, 400))


    def open(self):
        self.isOpened = True

    def close(self):
        self.isOpened = False
        self.file.export()
