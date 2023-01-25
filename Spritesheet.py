import pygame


class SpriteSheet:

    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()

    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha() #Creer une image transparente de la taille du rectangle
        image.blit(self.sheet, (0, 0), rect) #Peindre une partie du spritesheet sur l'image
        return image
    
    def images(self, rows, columns):
        #Coupe le spritesheet en lignes et colonnes et enregistre chaque image dans une liste
        xStep=self.sheet.get_width()/columns
        yStep=self.sheet.get_height()/rows
        cropped_images = []
        for xi in range(columns):
            for yi in range(rows):
                x=xi*xStep
                y=yi*yStep
                cropped_images.append(self.image_at(pygame.Rect(x, y, xStep, yStep)))
        return cropped_images
