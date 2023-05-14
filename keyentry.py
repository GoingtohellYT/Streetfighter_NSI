import pygame


class Keyentry:

    def __init__(self, optionmenu, entrytext, key, player, game, index):
        self.optionmenu = optionmenu
        self.entrytext = entrytext
        self.key = key
        self.index = index
        self.game = game
        self.player = player
        self.greyColor1 = (60, 60, 60)
        self.greyColor2 = (80, 80, 80)
        self.whiteColor = (240, 240, 240)
        self.state = 0  # 0: Normal, 1: Au dessus, 2: Selectionné

    def update(self, x, y, screen):
        rect = pygame.Rect(x + 350, y, 100, 30)

        # Code qui modifie l'état du rectangle
        if rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:  # Si on clique sur le carré - get_pressed renvoie une séquence de boolean pour chaque bouton de la souris
                self.state = 2  # On met l'état selectionné
            elif self.state == 0:
                self.state = 1  # La souris est au-dessus
        else:
            if self.state == 2 and pygame.mouse.get_pressed()[0]:  # Si on clique ailleurs
                self.state = 0  # on remet l'état en normal
            if self.state == 1:
                self.state = 0  # on remet l'état en normal

        if self.state == 2:
            for entry, isPressed in self.game.pressed.items():
                if isPressed:
                    self.key = entry
                    self.player.keys[self.index] = entry
                    self.state = 0

        text = self.optionmenu.font.render(self.entrytext, 1, self.whiteColor)
        screen.blit(text, (x,y))

        #Affiche le rectangle en fonction de son état
        color = self.greyColor1
        if self.state == 1:
            color = self.greyColor2
        elif self.state == 2:
            pygame.draw.rect(screen, self.whiteColor, rect.inflate(2,2)) # Dessine un rectangle blanc un tout petit peu plus grand: rect.inflate --> Grossis le rectangle
        pygame.draw.rect(screen, color, rect)

        keyText = self.optionmenu.smallFont.render(pygame.key.name(self.key), 1, self.whiteColor)
        textWidth, textHeight = self.optionmenu.smallFont.size(pygame.key.name(self.key)) # Recupère la longueur et largeur du texte à l'écran pour le centrer après
        screen.blit(keyText, (rect.x + (100-textWidth)/2, rect.y + (30-textHeight)/2))
