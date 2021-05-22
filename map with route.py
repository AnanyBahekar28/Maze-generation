import random
import sys
import pygame
import time
def check(array,cell):
    status=False
    for i in range (len(array)):
        if array[i]==cell:
            status=True
            break
    return status
pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((600, 600))
cell1 = pygame.image.load("cell1.png").convert()
cell2 = pygame.image.load("cell2.png").convert()
targetcel=pygame.image.load('targetcell.png')
background=pygame.image.load('background.png')
array = [cell1, cell2]
x = 0
y = 0
number = 1
blacknum = []
for b in range(8):
    for a in range(8):
        if number!=1 and number!=64:
            choice = random.choice(array)
            if choice == cell2:
                blacknum.append(number)
        number = number + 1

targetcell = 64
startcell = 1
currentcell = 1
randomlist = []
pathlist = [1]
direction = []
while currentcell != targetcell:
    randomlist.clear()
    direction.clear()
    if check(blacknum,currentcell+1)==False and (currentcell % 8) != 0 and check(pathlist,currentcell+1)==False:
                direction.append(currentcell + 1)
    if check(blacknum,currentcell-1)==False and (currentcell % 8) != 1 and check(pathlist,currentcell-1)==False:
                direction.append(currentcell - 1)
    if check(blacknum,currentcell+8)==False and int((currentcell + 8) / 8) < 8 and check(pathlist,currentcell+8)==False:
                direction.append(currentcell + 8)
    if check(blacknum,currentcell-8)==False and int((currentcell - 8)  / 8) > 1  and check(pathlist,currentcell-8)==False:
                direction.append(currentcell - 8)
    if len(direction) > 0:
        c = random.choice(direction)
        pathlist.append(c)
        currentcell = c
    if len(direction) <= 0:
        if (currentcell % 8) != 1 and check(pathlist,currentcell-1)==False:
            randomlist.append(currentcell - 1)
        if (currentcell % 8) != 0 and check(pathlist,currentcell+1)==False:
            randomlist.append(currentcell + 1)
        if  int((currentcell + 8) / 8) < 8 and check(pathlist,currentcell+8)==False:
            randomlist.append(currentcell + 8)
        if int((currentcell - 8)  / 8) > 1  and check(pathlist,currentcell-8)==False:
            randomlist.append(currentcell-8)
        choice=random.choice(randomlist)
        blacknum.remove(choice)
print(pathlist)
screen.blit(background,(0,0))
for i in range(len(pathlist)):
        screen.blit(cell1, ((((pathlist[i]) % 8) * 75) - 75, (((int((pathlist[i]) / 8)) * 75) - 75)))
        pygame.display.update()
for i in range(len(blacknum)):
        screen.blit(cell2, ((((blacknum[i]) % 8) * 75) - 75, (((int((blacknum[i]) / 8)) * 75) - 75)))
        pygame.display.update()

print(blacknum)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
