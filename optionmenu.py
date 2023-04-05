import pygame
from keyentry import Keyentry
from animation import Animation

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

        self.player1Entries.append(Keyentry(self,"Se déplacer vers la gauche : ", pygame.K_q,game.player_one, game))
        self.player1Entries.append(Keyentry(self, "Se déplacer vers la droite : ", pygame.K_d, game.player_one, game))
        self.player1Entries.append(Keyentry(self, "Sauter : ", pygame.K_z, game.player_one, game))
        self.player1Entries.append(Keyentry(self, "Attaque sautée : ", pygame.K_s, game.player_one, game))
        self.player1Entries.append(Keyentry(self, "Tirer : ", pygame.K_e, game.player_one, game))

        self.player2Entries.append(Keyentry(self, "Se déplacer vers la gauche : ", pygame.K_q, game.player_two, game))
        self.player2Entries.append(Keyentry(self, "Se déplacer vers la droite : ", pygame.K_d, game.player_two, game))
        self.player2Entries.append(Keyentry(self, "Sauter : ", pygame.K_z, game.player_two, game))
        self.player2Entries.append(Keyentry(self, "Attaque sautée : ", pygame.K_s, game.player_two, game))
        self.player2Entries.append(Keyentry(self, "Tirer : ", pygame.K_e, game.player_two, game))

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