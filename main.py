import pygame
from hero import Hero
from enemy import Enem
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
a = 0
coin = pygame.transform.scale(pygame.image.load('full-moon.png'), ((150,150)))
for_menu_window = pygame.display.set_mode((500,500))







window = pygame.display.set_mode((1000,1000))
enemy = Enem(1000//12,'stillLshark.png',5,window,400)
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load('1cadrfon.png'), ((1000,1000)))
hero = Hero(window)
hero.rect.y = 850
hero.rect.x = 500
ARIAL_50 = pygame.font.SysFont('Arial',50)

class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._curn_option_index = 0
    def append_option(self, option, callback):
        self._option_surfaces.append(ARIAL_50.render(option,True, (0,0,0)))
        self._callbacks.append(callback)


    def switch(self, direction):
        self._curn_option_index = max(0,min(self._curn_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._curn_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._curn_option_index:
                pygame.draw.rect(surf, (0, 100, 0),option_rect)
            surf.blit(option, option_rect)
menu = Menu()



def slide():
    menu.append_option('PLAY',lambda: print('because just start EASY SELECTED'))
    menu.append_option('QUIT',quit)
    menu.append_option('EASY',lambda: print('EASY SELECTED'))
    menu.append_option('MID',lambda: print('MID SELECTED'))
    menu.append_option('HARD',lambda: print(' HARD SELECTED'))
    menu.append_option('IMPOSIBLE',lambda: print('IMPOSIBLE SELECTED'))

cur_scene = None
def switch_scene(scene):
    global cur_scene
    cur_scene = scene
def scene1():
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False
                switch_scene(None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    menu.switch(-1)
                elif event.key == pygame.K_s:
                    menu.switch(1)
                elif event.key == pygame.K_SPACE:
                    menu.select()
                    switch_scene(scene2)
                    show = False

        pygame.display.flip()


slide()
for_menu_window.fill((0,0,255))

menu.draw(for_menu_window, 100, 100, 75)

pygame.display.flip()
def scene2():
    running = True
    a = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.blit(background, (0,0))
        if hero.rect.y < 5:
            background = pygame.transform.scale(pygame.image.load('peshera.png'), ((1000, 1000)))
            hero.rect.y = 900
            hero.rect.x = 400
            a += 1





        if hero.rect.x > 100 and hero.rect.x < 900 and hero.rect.y < 5 and a == 1:
            background = pygame.transform.scale(pygame.image.load('vtorifon.png'), ((1000, 1000)))
            hero.rect.x = 500
            hero.rect.y = 900
            a += 1
            enemy = Enem(1000 // 12, 'stillLshark.png', 5, window, 200)
        if hero.rect.y < 5 and a == 2:
            background = pygame.transform.scale(pygame.image.load('4fon.png'), ((1000, 1000)))
            hero.rect.x = 500
            hero.rect.y = 900
            a += 1
        if enemy.rect.colliderect(hero):
            break
        pygame.display.flip()
        hero.update()
        enemy.update()
        pygame.display.update()
        clock.tick(60)
switch_scene(scene1)
while cur_scene is not None:
    cur_scene()

