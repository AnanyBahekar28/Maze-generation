# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:35:51 2021

@author: Geeta
"""

import pygame
from pygame.locals import *
import random
import sys

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((600,600))
cell1 = pygame.image.load("cell1.png")
cell2 = pygame.image.load("cell2.png")
array = [cell1,cell2]
randomx = 0
randomy = 0
for b in range(8):
 for a in range(8):
  screen.blit(random.choice(array),(randomx,randomy))
  randomx = randomx+75
 randomx = 0
 randomy = randomy+75
screen.blit(cell1,(0,0))
screen.blit(cell1,(525,525))
x = 0
y = 0
previousx = 0
previousy = 0
def down():
    global x,y,previousy
    previousy = y
    y = y+75
    if y == 600:
        screen.blit(cell1,(x,previousy))
        y = previousy
    else:
     screen.blit(cell1,(x,y))
def right():
    global x,y,previousx
    previousx = x
    x = x+75
    if x == 600:
        screen.blit(cell1,(previousx,y))
        x = previousx
    else:
        screen.blit(cell1,(x,y))
fns = [down,right]
while (x,y) != (525,525):
 
 random.choice(fns)()
 pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        