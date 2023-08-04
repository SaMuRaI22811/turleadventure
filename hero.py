import pygame





class Hero:
    def __init__(self, window):
        self.K_w = [pygame.transform.scale(pygame.image.load('pixilart-drawing (1).png'), (170,170)),
                    pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170,170)),
                    pygame.transform.scale(pygame.image.load('pixilart-drawing (3).png'),(170, 170)),
                    pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170,170))]


        self.K_a = [pygame.transform.scale(pygame.image.load('pixilart-drawing (1).png'), (170, 70)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (3).png'),(170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170))]
        self.K_s = [
            pygame.transform.scale(pygame.image.load('pixilart-drawing (1).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (3).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170))]
        self.K_d = [
            pygame.transform.scale(pygame.image.load('pixilart-drawing (1).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (3).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170))]
        self.index = 0
        self.K_w = [pygame.transform.scale(pygame.image.load('pixilart-drawing (1).png'), (170,170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170,170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (3).png'),(170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170,170))]
        self.K_a = [pygame.transform.scale(pygame.image.load('pixilart-drawing (1).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (3).png'),(170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170))]
        self.K_s = [pygame.transform.scale(pygame.image.load('pixilart-drawing (1).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (3).png'),(170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170))]
        self.K_d = [pygame.transform.scale(pygame.image.load('pixilart-drawing (1).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (3).png'),(170, 170)),
            pygame.transform.scale(pygame.image.load('pixilart-drawing (2).png'), (170, 170))]
        self.window = window
        self.image = self.K_w[self.index]#pygame.transform.scale(pygame.image.load('turtle_walk_cut-photo_ru_(1)-transformed 1.png'), (130,130))
        self.rect = self.image.get_rect(center=(600, 400))
        self.speed = 3

#
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.image = self.K_w[self.index // 18]
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 900:
            self.image = self.K_s[self.index // 18]
            self.rect.y += self.speed
        if keys[pygame.K_d] and self.rect.x < 900:
            self.image = self.K_d[self.index // 18]
            self.rect.x += self.speed
        if keys[pygame.K_a] and self.rect.x > -50:
            self.image = self.K_a[self.index // 18]
            self.rect.x -= self.speed
        if self.index < 54:
            self.index += 1
        else:
            self.index = 0
        self.window.blit(self.image, self.rect)