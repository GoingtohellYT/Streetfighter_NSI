import pygame
from player import Player
from audio import SoundManager
from random import randint
from optionmenu import Optionmenu


# classe qui représente le jeu
class Game:

    def __init__(self):
        self.is_playing = False
        self.player_one_gr = pygame.sprite.Group()  # groupe de sprites qui contient les joueurs
        self.player_two_gr = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.player_one = Player(self, 1)  # crée une instance de la classe joueur pour notre joueur
        self.player_two = Player(self, 2)  # crée une seconde instance de la classe joueur
        self.player_one_gr.add(self.player_one)  # on ajoute notre joueur au groupe de sprites
        self.player_two_gr.add(self.player_two)
        self.pressed = {}
        self.controllers = list()
        self.sound_manager = SoundManager()
        self.timer = 180  # nombre de secondes maximal
        self.loop = 0  # nombre de boucles

        self.option = Optionmenu()

        # On initialise les deux manettes si possible
        pygame.joystick.init()
        try:
            self.joystick1 = pygame.joystick.Joystick(0)
            self.joystick2 = pygame.joystick.Joystick(1)
        except pygame.error:
            pass
        self.controller_count = pygame.joystick.get_count()
        if self.controller_count == 1 or self.controller_count > 2:
            self.controller_count = 0
            print("Veuillez jouer au clavier")

        # print(self.controller_count)

    def start(self):
        self.is_playing = True
        self.sound_manager.play("fight")
        print("Lancement du jeu")

    def game_over(self):
        self.is_playing = False  # affiche l'écran d'accueil
        # Annonce le vainqueur
        if self.player_one.health < self.player_two.health:
            self.sound_manager.play("p2_victory")
        elif self.player_two.health < self.player_one.health:
            self.sound_manager.play("p1_victory")
        # Remet les barres de vie des joueurs au maximum et remet les joueurs à leur position initiale.
        self.player_one.reset()
        self.player_two.reset()
        self.timer = 180
        self.loop = 0
        print("Arrêt du jeu")

    # On vérifie si les deux joueurs se touchent
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # On vérifie si le joueur adverse empêche notre joueur de se déplacer et on renvoie True si l'on peut bouger et False si le passage est bloqué.
    def check_positions(self, player, direction):
        if direction == "left":
            if player == 1:
                if self.player_one.rect.x <= self.player_two.rect.x:
                    return True
                else:
                    return False
            elif player == 2:
                if self.player_two.rect.x <= self.player_one.rect.x:
                    return True
                else:
                    return False
        elif direction == "right":
            if player == 1:
                if self.player_one.rect.x >= self.player_two.rect.x:
                    return True
                else:
                    return False
            elif player == 2:
                if self.player_two.rect.x >= self.player_one.rect.x:
                    return True
                else:
                    return False

    # Nouvelle fonction pour vérifier où est l'autre joueur et en déduire l'orientation du joueur lors de l'attaque
    def change_directions(self):
        if self.player_one.rect.x < self.player_two.rect.x:
            self.player_one.animation.left_direction = False
            self.player_two.animation.left_direction = True
            return "1-2"
        elif self.player_one.rect.x > self.player_two.rect.x:
            self.player_one.animation.left_direction = True
            self.player_two.animation.left_direction = False
            return "2-1"

    def update(self, screen):
        # On ajoute 1 au nombre de tours de boucle
        self.loop += 1
        # On vérifie si une seconde est passée
        if self.loop % 30 == 0:
            self.timer -= 1
            if self.timer == 0:
                self.game_over()

        # print(self.pressed)

        # On affiche le timer à l'écran
        font = pygame.font.SysFont("Bauhaus 93", 35)
        timer_text = font.render(str(self.timer) + "s", 1, (255, 0, 0))
        screen.blit(timer_text, (500, 10))

        # afficher les joueurs
        screen.blit(self.player_one.animation.get_current_image(), self.player_one.rect)
        self.player_one.update(1)
        screen.blit(self.player_two.animation.get_current_image(), self.player_two.rect)
        self.player_two.update(1)

        # afficher les barres de vie des joueurs et les actualiser.
        self.player_one.update_health_bar(screen)
        self.player_two.update_health_bar(screen)

        # Faire bouger tous les projectiles
        for projectile in self.projectiles:
            projectile.move()
            screen.blit(projectile.image, projectile.rect)  # Dessiner les projectiles à l'écran

        if self.player_one.animation.state != 2:
            if self.controller_count == 2:
                if self.joystick1.get_button(14) and self.player_one.rect.width + self.player_one.rect.x < screen.get_width():
                    self.player_one.animation.state = 1
                    self.player_one.animation.left_direction = False
                elif self.joystick1.get_button(13) and self.player_one.rect.x > 0:
                    self.player_one.animation.state = 1
                    self.player_one.animation.left_direction = True
                else:
                    self.player_one.animation.state = 0

                if self.joystick1.get_button(12):
                    self.player_one.increased_fall()

                if self.joystick1.get_button(3):
                    self.player_one.shoot_projectile()

                # vérifie si le joueur peut sauter (s'il touche le sol)
                if (self.joystick1.get_button(11) or self.joystick1.get_button(0)) and self.player_one.rect.y == self.player_one.default_y:
                    self.player_one.jump = 20

            elif self.controller_count == 0:
                # vérifier si le joueur 1 souhaite et peut se déplacer dans les limites de l'écran
                if self.pressed.get(
                        pygame.K_d) and self.player_one.rect.width + self.player_one.rect.x < screen.get_width():
                    self.player_one.animation.state = 1
                    self.player_one.animation.left_direction = False
                elif self.pressed.get(pygame.K_q) and self.player_one.rect.x > 0:
                    self.player_one.animation.state = 1
                    self.player_one.animation.left_direction = True
                else:
                    self.player_one.animation.state = 0

                if self.pressed.get(pygame.K_s):
                    self.player_one.increased_fall()

                if self.pressed.get(pygame.K_e):
                    self.player_one.shoot_projectile()

                # vérifie si le joueur peut sauter (s'il touche le sol)
                if self.pressed.get(pygame.K_z) and self.player_one.rect.y == self.player_one.default_y:
                    self.player_one.jump = 20

        # idem pour le joueur 2
        if self.player_two.animation.state != 2:
            if self.controller_count == 0:
                if self.pressed.get(
                        pygame.K_ASTERISK) and self.player_two.rect.width + self.player_two.rect.x < screen.get_width():
                    self.player_two.animation.state = 1
                    self.player_two.animation.left_direction = False
                elif self.pressed.get(pygame.K_m) and self.player_two.rect.x > 0:
                    self.player_two.animation.state = 1
                    self.player_two.animation.left_direction = True
                else:
                    self.player_two.animation.state = 0

                if self.pressed.get(249):
                    self.player_two.increased_fall()

                if self.pressed.get(36):
                    self.player_two.shoot_projectile()

                if self.pressed.get(pygame.K_CARET) and self.player_two.rect.y == self.player_two.default_y:
                    self.player_two.jump = 20

            elif self.controller_count == 2:
                if self.joystick2.get_button(
                        14) and self.player_two.rect.width + self.player_two.rect.x < screen.get_width():
                    self.player_two.animation.state = 1
                    self.player_two.animation.left_direction = False
                elif self.joystick2.get_button(13) and self.player_two.rect.x > 0:
                    self.player_two.animation.state = 1
                    self.player_two.animation.left_direction = True
                else:
                    self.player_two.animation.state = 0

                if self.joystick2.get_button(12):
                    self.player_two.increased_fall()

                if self.joystick2.get_button(3):
                    self.player_two.shoot_projectile()

                if (self.joystick2.get_button(11) or self.joystick2.get_button(0)) and self.player_two.rect.y == self.player_two.default_y:
                    self.player_two.jump = 20

    def attack(self, key, controller):
        self.change_directions()
        if key == pygame.K_SPACE or controller == "controller1":
            # On choisit aléatoirement un des deux sons d'attaque
            attack_sound = randint(1, 2)
            if attack_sound == 1:
                self.sound_manager.play("attack1")
            elif attack_sound == 2:
                self.sound_manager.play("attack2")
            # On déclenche l'attaque
            self.player_one.animation.state = 2  # Etat du joueur lorsqu'il frappe
            if self.check_collision(self.player_one, self.player_two_gr):
                self.player_two.damage(self.player_one.attack)
        elif key == pygame.K_INSERT or controller == 'controller2':
            # idem que pour joueur 1
            attack_sound = randint(1, 2)
            if attack_sound == 1:
                self.sound_manager.play("attack1")
            elif attack_sound == 2:
                self.sound_manager.play("attack2")
            # On déclenche l'attaque
            self.player_two.animation.state = 2  # Etat du joueur lorsqu'il frappe
            if self.check_collision(self.player_two, self.player_one_gr):
                self.player_one.damage(self.player_two.attack)

    def fall_attack(self, key):
        if key == pygame.K_s and self.check_collision(self.player_one, self.player_two_gr):
            self.player_two.damage(0.2 * self.player_one.attack)
        elif key == 249 and self.check_collision(self.player_two, self.player_one_gr):
            self.player_one.damage(0.2 * self.player_two.attack)
