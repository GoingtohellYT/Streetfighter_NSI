import pygame
from moviepy.editor import VideoFileClip
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
background = pygame.image.load('assets/background.png')
background = pygame.transform.scale(background, (1080, 720))

# on charge l'image du bouton quitter et on modifie sa taille
quit_btn = pygame.image.load('assets/quit_button.png')
quit_btn = pygame.transform.scale(quit_btn, (300, 100))
# on définit l'emplacement du bouton et sa hitbox
quit_btn_rect = quit_btn.get_rect()
quit_btn_rect.x = math.ceil((screen.get_width()-300) / 2)
quit_btn_rect.y = math.ceil((screen.get_height()-310) / 2+315)

# idem pour le bouton jouer
play_btn = pygame.image.load("assets/play_button.png")
play_btn = pygame.transform.scale(play_btn, (300, 100))
play_btn_rect = play_btn.get_rect()
play_btn_rect.x = math.ceil((screen.get_width()-300) / 2)
play_btn_rect.y = math.ceil((screen.get_height()-310) / 2)

# idem pour le bouton option
option_btn = pygame.image.load("assets/option_button.png")
option_btn = pygame.transform.scale(option_btn, (300, 100))
option_btn_rect = option_btn.get_rect()
option_btn_rect.x = math.ceil((screen.get_width()-300) / 2)
option_btn_rect.y = math.ceil((screen.get_height()-310) / 2+105)

# idem pour le bouton crédits
credits_btn = pygame.image.load("assets/credit_btn.png")
credits_btn = pygame.transform.scale(credits_btn, (300, 100))
credits_btn_rect = credits_btn.get_rect()
credits_btn_rect.x = math.ceil((screen.get_width()-300) / 2)
credits_btn_rect.y = math.ceil((screen.get_height()-310) / 2+210)


# idem pour le bouton Retour en arrière
back_btn = pygame.image.load("assets/back_button.png")
back_btn = pygame.transform.scale(back_btn, (60, 60))
back_btn_rect = back_btn.get_rect()
back_btn_rect.x = 5
back_btn_rect.y = 5

clip = VideoFileClip("assets/videos/creditsEasterEgg.mp4")

game = Game()  # On charge la classe du jeu

running = True
while running:
    # on affiche le fond
    screen.blit(background, (0, 0))
    if game.option.isOpened:
        game.option.update(screen)
        screen.blit(back_btn, back_btn_rect)
    elif game.is_playing:
        game.update(screen)
    else:
        # ajouter l'écran de bienvenue
        screen.blit(quit_btn, quit_btn_rect)
        screen.blit(option_btn, option_btn_rect)
        screen.blit(play_btn, play_btn_rect)
        screen.blit(credits_btn, credits_btn_rect)

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
            if not game.is_playing and not game.option.isOpened:
                if quit_btn_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
                elif play_btn_rect.collidepoint(event.pos):
                    game.start()
                elif option_btn_rect.collidepoint(event.pos):
                    game.option.open()
                elif credits_btn_rect.collidepoint(event.pos):
                    clip.preview()
                    pygame.quit()
                    exit()
            if back_btn_rect.collidepoint(event.pos) and game.option.isOpened:
                game.option.close()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True  # on ajoute la touche pressée au dict
            game.attack(event.key, None)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False  # on retire la touche pressée du dict

        elif event.type == pygame.JOYBUTTONDOWN and game.controller_count != 0:
            game.pressed[event.button] = True

            # Si le bouton pressé correspond à l'attaque
            if event.button == pygame.CONTROLLER_BUTTON_X:
                if game.joystick1.get_button(2):
                    game.attack(None, "controller1")
                if game.joystick2.get_button(2):
                    game.attack(None, 'controller2')

        elif event.type == pygame.JOYBUTTONUP:
            game.pressed[event.button] = False

    clock.tick(FPS)
