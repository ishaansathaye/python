import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.right = True
        image = pygame.image.load("Exploration Project/images/walking_character_v3.png").convert_alpha()
        width = 60 # have the students add this.
        height = 104
        self.images = [image.subsurface(0, 0, 60, 104), image.subsurface(60, 0, 60, 104), image.subsurface(120, 0, 60, 104)]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(100, 190))
        self.count = 0

    def update(self):
        if self.count < 2:
            self.count += 1
        else:
            self.count = 0
        self.image = self.images[self.count]
        player_speed = 10
        if self.right:
            self.rect.x += player_speed
        else:
            self.rect.x -= player_speed

        if(self.rect.x > 570):
            self.switch_dir()
        if(self.rect.x < 0):
            self.switch_dir()

    def switch_dir(self):
        if self.right:
            self.rect.x -= 10
            self.right = False
        else:
            self.right = True
            self.rect.x += 10