import pygame
import random

pygame.init()

WIDTH = 650
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the hero
hero = pygame.sprite.Sprite()

# Add image and rectangle properties to the hero
hero.image = pygame.image.load('hero.png')
hero.rect = hero.image.get_rect()

#Tile constants
TILE_SIZE = hero.rect.width
NUM_TILES_WIDTH = int(WIDTH / TILE_SIZE)
NUM_TILES_HEIGHT = int(HEIGHT / TILE_SIZE)

candies = pygame.sprite.OrderedUpdates() #Make a list to store the candies
for i in range (10):
    candy = pygame.sprite.Sprite() #Make a sprite for 1 candy
    candy.image = pygame.image.load('candy.png') #Load an image into the sprite
    candy.rect = candy.image.get_rect() #Get a rectangle from the image
    #Position the candy
    candy.rect.left = random.randint(0, NUM_TILES_WIDTH - 1) * TILE_SIZE
    candy.rect.top = random.randint(0, NUM_TILES_HEIGHT - 1) * TILE_SIZE
    candies.add(candy) #Add it to the list of candies

#Sprite Groups
hero_group = pygame.sprite.GroupSingle(hero)

#Loop conditions
finish = False
win = False
#Main Loop
while finish != True:
    #Event Loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Move the hero around the screen
            if event.key == pygame.K_UP:
                hero.rect.top -= TILE_SIZE
            elif event.key == pygame.K_DOWN:
                hero.rect.top += TILE_SIZE
            elif event.key == pygame.K_RIGHT:
                hero.rect.right += TILE_SIZE
            elif event.key == pygame.K_LEFT:
                hero.rect.right -= TILE_SIZE
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finish = True
    #Check for a collision and remove the candy if there is one
    pygame.sprite.groupcollide(hero_group, candies, False, True)
    #Check if we're out of candy
    if len(candies) == 0:
        win = True

    # Paint the background black (the three values represent red, green and blue: 0 for all of them makes it black)
    screen.fill((0, 0, 0))
    candies.draw(screen)
    hero_group.draw(screen)
    if win:
        font = pygame.font.Font(None, 36)
        text_image = font.render("You Win!", True, (255, 255, 255))
        text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100)
        screen.blit(text_image, text_rect)
    pygame.display.update()

pygame.quit()








