# my_pygames
# my_pygames
this is my first game with pygame in python.
- What is it about?
- How does it work?
- Do i need to download something?????
  you dont to install anything. But you need to install pygame(that's it)
  watch a tutorial that tells you how to install it
-please like it, i have even better games comming

  -_-_-_-_-_-_-_-_-_-
   All the stuff about it:
  _-_-_-_-_-_-_-_-_-_

import pygame
import random
#you just import pygame and random for a lot of stuff.

pygame.init()
#initialize pygame

#for screen
screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()
#why "screen"? Its to adjust the width and the height of the screen
#clock is for ticks.(its important for later)

run = True
#True means that if the code is running(or the game is running) then this happens

while run:
    #you need to understand this.
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False
        #this means that if you press the x button that's up of your screen(not phones and other          stuff like that), you exit the game.
#you understand this ok? 
keys = pygame.key.get_pressed()

#if you press that button, the game will stop
if keys[pygame.K_ESCAPE]:
    break

#you need to understand this or learn english better
if keys[pygame.K_a]:
    player.x -= 5
if keys[pygame.K_d]:
    player.x += 5
if keys[pygame.K_w]:
    player.y -= 5
if keys[pygame.K_s]:
    player.y += 5

#player = to all of this thing. w(width)-player.width with player.x
player.x = max(0, min(w-player.width, player.x))

item.y += 5
    #if the item.y is higher than the h(height)
    if item.y > h:
        #it will make the blocks spawn somewhere at the top of the screen
        item.x = random.randint(0, w-20)
        #i dont know
        item.y = -20
#if the player collides with the item
if player.colliderect(item):
        #s
        score += 50
        screen.blit(pygame.font.SysFont(None, 40).render(f"Score: {score}", True,<--- |   ((255,255,255)), (10,10))<--#this is also part of this--------------------------------|
#to add the score with the type of font in pygame

#to make the block spawn somewhere up
item.x = random.randint(0, w-20)
        item.y = -20
        
#its rgb for that line
screen.fill((40,40,50))
    #to draw the player and the blocks
    pygame.draw.rect(screen, (0,200,255), player)
    pygame.draw.rect(screen, (255,255,0), item)
    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10,10))

#to update the whole thing(and i mean everything)
  pygame.display.flip()
  #for speed and the tick
  clock.tick(60)

#to leave pygame.
  pygame.quit()

  --------------------
  that's all. hope you will like my game!
  comment if you find some errors!
  --------------------

  ..YOU                                                      ME..
  /( 'o')\ :(i wonder if the game is good!) (Yes it is!): /(0-0 )\
