import pygame

class Enem(pygame.sprite.Sprite):
    def __init__(self,x,filename,speed,window,y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(filename), ((200,200)))
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = speed
        self.window = window

    def update(self):
        self.window.blit(self.image, self.rect)
        self.rect.x -= self.speed
        self.image = pygame.transform.scale(pygame.image.load('stillLshark.png'), ((200,150)))
        if self.rect.x < 5:
            self.rect.x = 900


