import pygame
import random

w, h = 400, 500
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()


item = pygame.Rect(random.randint(0, w-20), -20, 20, 20)
score = 0

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        break


    if keys[pygame.K_a]:
        player.x -= 5
    if keys[pygame.K_d]:
        player.x += 5
    if keys[pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_s]:
        player.y += 5
        

    player.x = max(0, min(w-player.width, player.x))

    item.y += 5
    if item.y > h:
        item.x = random.randint(0, w-20)
        item.y = -20

    if player.colliderect(item):
        score += 50
        screen.blit(pygame.font.SysFont(None, 40).render(f"Score: {score}", True, (255,255,255)), (10,10))

        item.x = random.randint(0, w-20)
        item.y = -20

    screen.fill((40,40,50))
    pygame.draw.rect(screen, (0,200,255), player)
    pygame.draw.rect(screen, (255,255,0), item)
    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10,10))

    pygame.display.flip()
    clock.tick(60)


pygame.quit()

