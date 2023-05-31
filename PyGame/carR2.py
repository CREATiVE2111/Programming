import pygame
class carR(pygame.sprite.Sprite):
    def __init__(self, z, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(z, -300))
        self.speed = speed
        self.add(group)
    def update(self, *args):
        if self.rect.y < args[0]:
            self.rect.y += self.speed
        else:
            self.kill()