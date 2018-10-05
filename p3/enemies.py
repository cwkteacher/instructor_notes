import pygame


# base enemy class, inherits from the pygame Sprite class
class Enemy(pygame.sprite.Sprite):

    # constructor, takes a tuple with a position and optionally an image path and speed list
    def __init__(self, pos, image="images/enemy.png", speed=[0, 3]):
        # call the Sprite class constructor
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = speed

    # move the enemy
    def update(self, *args):
        self.rect.move_ip(self.speed)
        # remove the enemy if it goes off screen
        if self.rect.y > pygame.display.Info().current_h:
            self.kill()


class FiringEnemy(Enemy):

    def __init__(self, pos):
        super().__init__(pos, "images/firing_enemy.png", [0, 1])
        self.recharge = 0
        self.fire_time = 120

    def update(self, *args):
        super().update()
        self.recharge += 1
        if self.recharge > self.fire_time:
            self.fire()
            self.recharge = 0

    def fire(self):
        self.groups()[0].add(Enemy(self.rect.midbottom, "images/laser.png", [0, 5]))
