from Spritesheet import SpriteSheet
import pygame

class animation:
    def __init__(self, nb):
        self.state=0 #Etat du joueur (0: Ne bouge pas, 1: est entrain de marcher)
        self.left_direction=False #Va à gauche ou à droite
        self.frame_rate = 4 #L'animation du joueur change toutes les 4 frames
        self.current_frame = 0
        spritesheet = SpriteSheet('assets/player'+str(nb)+'_idle.png')
        self.player_idle_images = spritesheet.images(1,6) #Découpe les images du joueur
        spritesheet = SpriteSheet('assets/player'+str(nb)+'_walk.png')
        self.player_walk_images = spritesheet.images(1,6) #Découpe les images du joueur

        #Redimensionner chaque image individuellement
        for i in range(len(self.player_idle_images)):
            self.player_idle_images[i] = pygame.transform.scale(self.player_idle_images[i], (60,120))
        for i in range(len(self.player_walk_images)):
            self.player_walk_images[i] = pygame.transform.scale(self.player_walk_images[i], (60, 120))

        self.player_idle_index = 0
        self.player_walk_index = 0

    def get_current_image(self):
        current_image = self.player_idle_images[self.player_idle_index]
        if self.state == 1:
            current_image = self.player_walk_images[self.player_walk_index]
            if self.left_direction:
                current_image = pygame.transform.flip(current_image, True, False) #Retourne l'image si le joueur va à gauche
        return current_image

    def update(self):
        self.current_frame+=1
        if self.frame_rate == self.current_frame:
            self.current_frame = 0;
            if self.state==0:
                self.player_idle_index = self.update_index(self.player_idle_index, 6)
            elif self.state==1:
                self.player_walk_index = self.update_index(self.player_walk_index, 6)

    def update_index(self, index, indexMax):
        index = index+1
        if index>=indexMax:
            index=0
        return index
