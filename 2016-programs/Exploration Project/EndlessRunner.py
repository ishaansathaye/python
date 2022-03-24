#Created August 12, 2016 at 2:27 PM
#Complete Source Code - Bubble Buster.
#Expand this box to see all of the code.
import pygame
import sys
from pygame.locals import *
from Player import Player

pygame.init()

screen = pygame.display.set_mode((640, 460))

background = pygame.image.load("Exploration Project/images/cave_background.png").convert_alpha();
background2 = pygame.image.load("Exploration Project/images/cave_background.png").convert_alpha();
screen.blit(background, (0, 0))

pygame.display.set_caption('Bouncer')
font = pygame.font.SysFont(None, 36)

player = Player()

bouncing_group = pygame.sprite.Group()
bouncing_group.add(player)

main_clock = pygame.time.Clock()

x = 0
y = 0

x1 = background.get_size()[0] - 8
y1 = 0

width = x1

def move_backgrounds():
    global x, x1, background, right_pos
    if x < -width:
        x =  width;
    if x1 < -width:
        x1 = width
    x -= 3
    x1 -= 3

timer = 0
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Ensure consistent frames per second
    main_clock.tick(120)
    screen.blit(background, (x, y))
    screen.blit(background2, (x1, y1))
    bouncing_group.clear(background, background)
    bouncing_group.clear(background2, background2)
    bouncing_group.draw(screen)
    move_backgrounds()

    timer += 1
    if timer > 10:
        bouncing_group.update()
        timer = 0

    pygame.display.update()
