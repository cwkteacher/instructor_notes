import pygame, random, sys
from pygame.locals import *
from player import Player
from enemies import Enemy, FiringEnemy

pygame.init()

# sets width and height to the dimensions of any screen
size = (width, height) = (700, 700)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
# Sprite Groups for this game
player = pygame.sprite.GroupSingle()
enemies = pygame.sprite.Group()


def main():
    global screen
    # interval at which enemies should spawn in milliseconds
    spawn_interval = 3000
    # variable to store the last spawn time
    last_spawned = 0
    game_over = False
    # add a Player object to the player group
    player.add(Player((width//2, height-50)))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                # screen controls
                if event.key == K_f:
                    screen = pygame.display.set_mode(size, FULLSCREEN)
                elif event.key == K_ESCAPE:
                    screen = pygame.display.set_mode(size)
        if not game_over:
            # controls, checks for currently pressed keys
            keys = pygame.key.get_pressed()
            if keys[K_RIGHT]:
                player.sprite.right()
            if keys[K_LEFT]:
                player.sprite.left()
            # check if it is time to spawn an enemy
            if pygame.time.get_ticks() - spawn_interval > last_spawned:
                last_spawned = pygame.time.get_ticks()
                # spawn a normal enemy 80% of the time
                if random.randint(1, 100) < 80:
                    enemies.add(Enemy((random.randint(50, width - 50), -100)))
                else:
                    # spawn a Firing Enemy
                    enemies.add(FiringEnemy((random.randint(50, width - 50), -100)))
        # update the sprite groups
        enemies.update()
        player.update(enemies)   # pass in enemy group for collision handling
        # check if the game is over
        if len(player) == 0:
            game_over = True
        screen.fill(color)
        player.draw(screen)
        enemies.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
