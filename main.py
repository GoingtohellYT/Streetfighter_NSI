import pygame
from game import Game
import math

pygame.init()

# définir une clock
clock = pygame.time.Clock()
FPS = 30

# génération de la fenêtre de jeu
pygame.display.set_caption("Fight !")
screen = pygame.display.set_mode((1080, 720))

# on récupère l'image de fond et on modifie sa taille
background = pygame.image.load('assets/bg.png')
background = pygame.transform.scale(background, (1080, 720))

# on charge l'image du bouton quitter et on modifie sa taille
quit_btn = pygame.image.load('assets/quit.png')
quit_btn = pygame.transform.scale(quit_btn, (300, 100))
# on définit l'emplacement du bouton et sa hitbox
quit_btn_rect = quit_btn.get_rect()
quit_btn_rect.x = math.ceil(screen.get_width() / 2.9)
quit_btn_rect.y = math.ceil(screen.get_height() / 1.4)

# idem que pour le bouton quitter
play_btn = pygame.image.load("assets/button.png")
play_btn = pygame.transform.scale(play_btn, (400, 150))
play_btn_rect = play_btn.get_rect()
play_btn_rect.x = math.ceil(screen.get_width() / 3.33)
play_btn_rect.y = math.ceil(screen.get_height() / 2)


game = Game()  # On charge la classe du jeu

running = True
while running:
    # on affiche le fond
    screen.blit(background, (0, 0))
    if game.is_playing:
        game.update(screen)
    else:
        # ajouter l'écran de bienvenue
        screen.blit(quit_btn, quit_btn_rect)
        screen.blit(play_btn, play_btn_rect)

    # mettre l'écran à jour
    pygame.display.flip()

    for event in pygame.event.get():
        # Si le joueur ferme la fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # si le joueur clique sur le bouton pour quitter
            if quit_btn_rect.collidepoint(event.pos):
                pygame.quit()
                exit()

            elif play_btn_rect.collidepoint(event.pos):
                game.start()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True  # on ajoute la touche pressée au dict

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False  # on retire la touche pressée du dict

    clock.tick(FPS)
