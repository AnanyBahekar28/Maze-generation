import random
import sys
import pygame
import time

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((600, 600))
cell1 = pygame.image.load("cell1.png").convert()
cell2 = pygame.image.load("cell2.png").convert()
array = [cell1, cell2]
x = 0
y = 0
number = 1
blacknum = []
for b in range(8):
    for a in range(8):
        choice = random.choice(array)
        screen.blit(choice, (x, y))
        if choice == cell2:
            blacknum.append(number)
        x = x + 75
        number = number + 1
    x = 0
    y = y + 75
targetcell = 64
startcell = 1
currentcell = 1
randomlist = []
pathlist = []
direction = []
while currentcell != targetcell:
    randomlist.clear()
    direction.clear()
    if (currentcell + 1) != all(blacknum) and (currentcell % 8) < 8 and currentcell+1!=all(pathlist):
                direction.append(currentcell + 1)
    if (currentcell - 1) != all(blacknum) and (currentcell % 8) > 1 and (currentcell - 1) != all(pathlist):
                direction.append(currentcell - 1)
    if (currentcell + 8) != all(blacknum) and (currentcell + 8) <= 64 and (currentcell + 8) != all(pathlist):
                direction.append(currentcell + 8)
    if (currentcell - 8) != all(blacknum) and (currentcell - 8) > 0 and (currentcell - 8) != all(pathlist):
                direction.append(currentcell - 8)
    if len(direction) > 0:
        c = random.choice(direction)
        pathlist.append(c)
        currentcell = c
    if len(direction) <= 0:
        if all(pathlist) != currentcell - 1:
            randomlist.append(currentcell - 1)
        if all(pathlist) != currentcell + 1:
            randomlist.append(currentcell + 1)
        if all(pathlist) != currentcell + 8:
            randomlist.append(currentcell + 8)
        if all(pathlist) != currentcell - 8:
            randomlist.append(currentcell-8)
        for i in range(len(randomlist)):
            choic = random.choice(array)
            if ((randomlist[i]) % 8) > 0:
                screen.blit(choic, ((((pathlist[i]) % 8) * 75) - 75, ((((int((pathlist[i]) / 8)) + 1) * 75) - 75)))
                if choic == cell1:
                    blacknum.remove(randomlist[i])
            if ((randomlist[i]) % 8) <= 0:
                screen.blit(choic, (((int((pathlist[i]) / 8)) * 75) - 75, ((((pathlist[i]) % 8) * 75) - 75)))
                if choic == cell1:
                    blacknum.remove(randomlist[i])

    for i in range(len(pathlist)):
        if ((pathlist[i]) % 8) > 0:
            screen.blit(cell1, ((((pathlist[i]) % 8) * 75) - 75, ((((int((pathlist[i]) / 8)) + 1) * 75) - 75)))
        else:
            screen.blit(cell1, (((int((pathlist[i]) / 8)) * 75) - 75, ((((pathlist[i]) % 8) * 75) - 75)))
print(pathlist)
for i in range(len(pathlist)):
    if ((pathlist[i]) % 8) > 0:
        screen.blit(cell1, ((((pathlist[i]) % 8) * 75) - 75, ((((int((pathlist[i]) / 8)) + 1) * 75) - 75)))
    else:
        screen.blit(cell1, (((int((pathlist[i]) / 8)) * 75) - 75, ((((pathlist[i]) % 8) * 75) - 75)))
    pygame.display.update()

screen.blit(cell1, (0, 0))
screen.blit(cell1, (525, 525))
pygame.display.update()
print(blacknum)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
