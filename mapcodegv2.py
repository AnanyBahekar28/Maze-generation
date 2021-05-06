# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:46:35 2021

@author: Geeta
"""

import pygame
from pygame.locals import *
import random
import sys

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((600,600))
cell1 = (255,255,255)
cell2 = (220,220,220)
array = [cell1,cell2]
randomx = 0
randomy = 0
cellwidth = (600 / int(input("Enter the number of cells per row:")))
for b in range (int(600/cellwidth)):
 for a in range(int(600/cellwidth)):
  pygame.draw.rect(screen,(random.choice(array)),pygame.Rect(randomx,randomy,cellwidth,cellwidth))
  randomx = randomx + cellwidth
 randomx = 0
 randomy = randomy + cellwidth
pygame.draw.rect(screen,cell1,pygame.Rect(0,0,cellwidth,cellwidth))
pygame.draw.rect(screen,cell1,pygame.Rect((600 - cellwidth),(600 - cellwidth),cellwidth,cellwidth))
x = 0
y = 0
previousx = 0
previousy = 0
def down():
    global x,y,previousy
    previousy = y
    y = y + cellwidth
    if y == 600:
        pygame.draw.rect(screen,cell1,(x,previousy,cellwidth,cellwidth))
        y = previousy
    else:
     pygame.draw.rect(screen,cell1,pygame.Rect(x,y,cellwidth,cellwidth))
def right():
    global x,y,previousx
    previousx = x
    x = x + cellwidth
    if x == 600:
        pygame.draw.rect(screen,cell1,pygame.Rect(previousx,y,cellwidth,cellwidth))
        x = previousx
    else:
        pygame.draw.rect(screen,cell1,pygame.Rect(x,y,cellwidth,cellwidth))
fns = [down,right]
while (x,y) != ((600 - cellwidth),(600 - cellwidth)):
 random.choice(fns)()
 pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
"""
note: whenever the number of cells entered is not a factor of 600, 
Pygame crashes. A solution would be to use different sizes for the main 
screen.
"""