#Created October 15, 2015 at 10:28 AM
#Complete Snake Game Code.

#Import necessary libraries
import pygame
import sys
from pygame.locals import *

#Setting up PyGame and the game screen.
pygame.init()

screen_width = 640
screen_height = 460

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))
pygame.display.set_caption('Snake')
font = pygame.font.SysFont(None, 36)

#Open the map file.
map = open('Snake/map_char.txt', 'r')

#Create an initial x position, and an initial y position
x_pos = 0
y_pos = 0

#Size of the player squares, and spacing of items
size = 32

#Lists to hold map edges and food
map_edges = []
foods = []

#A list of all the pieces of the player
player = []

#Reads a text file
for line in map:
    line = line.rstrip()
    line = line.replace(" ", "")
    for x in range(0, len(line)):
        #Creates a map edge whenever it reads '#'.
        if line[x] == '#':
            rectangle = pygame.draw.rect(screen, (0, 0, 0), (x_pos, y_pos, size, size))
            map_edges.append(rectangle)
            x_pos += size
        #Creates a blank space when it reads '.'.
        elif line[x] == '.':
            x_pos += size
        #Creates the player snake when it reads an 'S'.
        elif line[x] == 'S':
            #Adds the player's head.
            player_head = pygame.Rect(x_pos, y_pos, size, size)
            x_pos += size
        #Creates a food square when it reads an 'f'.
        elif line[x] == 'f':
            food = pygame.draw.rect(screen, (0, 0, 0), (x_pos, y_pos, size, size))
            foods.append(food)
            x_pos += size
        else:
            pass
    x_pos = 0
    y_pos += size

map.close()

#Builds the player, sets its speed, and makes it alive.
player.append(player_head)
alive = True
player_speed = 200


main_clock = pygame.time.Clock()

snake_sections = 0

move_distance = size;

direction = [1, 0]

#Moves the player by popping an element out, repositioning it, and adding it back to the player list.
def move_player():
    if alive:
        player_head = player.pop()
        if len(player) == 0:
            player_head = pygame.Rect(player_head.x + (size * direction[0]), player_head.y + (size * direction[1]), size, size)
        else:
            player_head = pygame.Rect(player[0].x + (size * direction[0]), player[0].y + (size * direction[1]), size, size)
        player.insert(0, player_head)

timer = 0

while True:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #Move left
            if event.key == pygame.K_a and direction[0] != 1:
                direction = [-1, 0]
            #Move right
            if event.key == pygame.K_d and direction[0] != -1:
                direction = [1, 0]
            #Move up
            if event.key == pygame.K_w and direction[1] != 1:
                direction = [0, -1]
            #Move down
            if event.key == pygame.K_s and direction[1] != -1:
                direction = [0, 1]
            #Resets the player and level.
            if event.key == pygame.K_p:
                direction = [1, 0]
                player = player[:1]
                player[0] = pygame.Rect(size, size, size, size)
                alive = True

    main_clock.tick(50)

    #Increases a timer by a small amount.
    timer += main_clock.get_time()

    #Moves the player, and adds a new section if the player hit food.
    if timer > player_speed:
        if len(player) < snake_sections + 1:
            player_piece = pygame.Rect(player_head.x, player_head.y, size, size)
            player.append(player_piece)
        move_player()
        timer = 0

    #Draws the background.
    screen.fill((255, 255, 255))

    #Draws the player, map, and food if the player is alive.
    if alive:
        for x in range(0, len(player)):
            pygame.draw.rect(screen, (0, 0, 0), player[x])

        for rectangle in map_edges:
            if player[0].colliderect(rectangle):
                alive = False
            pygame.draw.rect(screen, (100, 0, 100), rectangle)

        for section in player:
            if section is not player[0]:
                if player[0].colliderect(section):
                    alive = False

        for food in foods:
            if player[0].colliderect(food):
                snake_sections += 1
                foods.remove(food)
            pygame.draw.rect(screen, (0, 0, 255), food)

    pygame.display.update()