from Spritesheet import SpriteSheet
import pygame

class animation:
    def __init__(self):
        self.state=1
        self.left_direction=False
        self.frame_rate = 4
        self.current_frame = 0
        spritesheet = SpriteSheet('assets/player1_idle.png')
        self.player_idle_images = spritesheet.images(1,6)
        spritesheet = SpriteSheet('assets/player1_walk.png')
        self.player_walk_images = spritesheet.images(1,6)

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
                current_image = pygame.transform.flip(current_image, True, False)
        return current_image

    def update(self):
        self.current_frame+=1
        if self.frame_rate == self.current_frame:
            self.current_frame = 0;
            if self.state==0:
                self.player_idle_index = self.update_index(self.player_idle_index, 6)
            elif self.state==1:
                self.player_walk_index = self.update_index(self.player_walk_index, 6)

    def update_index(self, index, max):
        index = index+1
        if index>=max:
            index=0
        return index
