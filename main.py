import pygame
from game import Game

pygame.init()

# définir une clock
clock = pygame.time.Clock()
FPS = 30

# génération de la fenêtre de jeu
pygame.display.set_caption("Fight !")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.png')
background = pygame.transform.scale(background, (1080, 720))

quit_btn = pygame.image.load('assets/quit.png')
quit_btn = pygame.transform.scale(quit_btn, (150, 50))

game = Game()  # On charge la classe du jeu

running = True
while running:
    screen.blit(background, (0, 0))
    if game.is_playing:
        pass
    else:
        # ajouter l'écran de bienvenue
        screen.blit(quit_btn, (700, 600))

    # mettre l'écran à jour
    pygame.display.flip()

    for event in pygame.event.get():
        # Si le joueur ferme la fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
