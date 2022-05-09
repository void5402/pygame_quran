# import  and start pygame package
import pygame
import os
from pathlib import Path
path = os.path.dirname(os.path.realpath(__file__))
pygame.init()
display_surface = pygame.display.set_mode((410, 520))
white = (255, 255, 255)
running = True
pygame.display.set_caption('قرآن')
display_surface.fill(white)
#defs for new image and others
cp = 1
icon = pygame.image.load(rf'{path}\icon.jpg')
pygame.display.set_icon(icon)
height = display_surface.get_height()
width = display_surface.get_width()
image = pygame.image.load(rf'{path}\images\{cp}.png')
display_surface.blit(image, (20, 0))

def icons(path):
    icon2 = pygame.image.load(rf'{path}\icon2.png')
    icon3 = pygame.image.load(rf'{path}\icon3.png')
    display_surface.blit(icon2, (365, 220))
    display_surface.blit(icon3, (0, 220))
def next_image(cp, path):
    image = pygame.image.load(rf'{path}\images\{cp}.png')
    display_surface.blit(image, (20, 0))
    icons(path)
    pygame.display.update() 
def back_image(cp, path):
    image = pygame.image.load(rf'{path}\images\{cp}.png')
    display_surface.blit(image, (20, 0))
    icons(path)
    pygame.display.update()
icons(path)
pygame.display.update() 
#45 65 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(mouse)
            if 365 <= mouse[0] <= 410 and 220 <= mouse[1] <= 285:
                print('next')
                cp = cp + 1
                my_file = Path(rf'{path}\images\{cp}.png')
                if my_file.is_file():
                 next_image(cp, path)
                else:
                 cp = cp - 1
                print(cp)
            if 0 <= mouse[0] <= 45 and 220 <= mouse[1] <= 285:
                print('back')
                cp = cp - 1
                if cp != 0:
                 back_image(cp, path)
                else:
                 cp = cp + 1
                print(cp)