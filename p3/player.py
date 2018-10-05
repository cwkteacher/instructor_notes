import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.dx = 0

    def update(self, enemies):
        self.rect.move_ip(self.dx, 0)
        # check if the sprite is off screen and move it back
        if self.rect.left < 0 or self.rect.right > pygame.display.Info().current_w:
            self.rect.move_ip(-self.dx, 0)
        # decrease the horizontal movement
        self.dx *= .9
        # check for collisions
        if len(pygame.sprite.spritecollide(self, enemies, True)):
            self.kill()

    # change dx so the sprite will move left
    def left(self):
        self.dx = -5

    # change dx so the sprite will move right
    def right(self):
        self.dx = 5
