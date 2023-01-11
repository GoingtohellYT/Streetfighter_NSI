import pygame


class SpriteSheet:

    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()


    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return image
    
    def images(self, rows, columns):
        x=0
        y=0
        xStep=self.sheet.get_width()/columns
        yStep=self.sheet.get_height()/rows
        cropped_images = []
        for xi in range(columns):
            for yi in range(rows):
                x=xi*xStep
                y=yi*yStep
                cropped_images.append(image_at(pygame.Rect(x,y,xStep,yStep)))
        return cropped_images