import random
import sys
import pygame
import time

def checkflodfill(array, cell):
    list = []
    for i in range(len(array)):
        if array[(i)] == cell:
            list.append(i)
    return list
def check(array,cell):
    status=False
    for i in range (len(array)):
        if array[i]==cell:
            status=True
            break
    return status
def display(list,sleep,image):
    for i in range(len(list)):
        x = (((list[i] - 1) % 8) * 75)
        y = ((int((list[i] - 1) / 8)) * 75)
        screen.blit(image, (x, y))
        pygame.display.update()
        time.sleep(sleep)

def priority(optionlist,destination,current):
    best=[]
    possible=[]
    current_x=(((current - 1) % 8) * 75)
    current_y=((int((current - 1) / 8)) * 75)
    destination_y=((int((destination - 1) / 8)) * 75)
    destination_x=(((destination - 1) % 8) * 75)
    x=current_x-destination_x
    y=current_y-destination_y
    if x>0:
       best.append(current-1)
    if x<0:
        best.append(current+1)
    if y>0:
        best.append(current-8)
    if y<0:
        best.append(current+8)
    for i in range(len(best)):
        d=check(optionlist,best[i])
        if d==True:
            possible.append(best[i])
            break
    if len(possible)>0:
        return possible[0]
    if len(possible)==0:
        return optionlist[0]

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
fblacknum=[]
for b in range(8):
    for a in range(8):
        if number!=1 and number!=64:
            choice = random.choice(array)
            if choice == cell2:
                blacknum.append(number)
                fblacknum.append(number)
        number = number + 1

targetcell = 64
startcell = 1
currentcell = 1
randomlist = []
pathlist = [1]
direction = []
fpathlist=[1]
while currentcell != targetcell:
    randomlist.clear()
    direction.clear()
    if check(fblacknum,currentcell+1)==False and (currentcell % 8) != 0 and check(pathlist,currentcell+1)==False:
                direction.append(currentcell + 1)
    if check(fblacknum,currentcell-1)==False and (currentcell % 8) != 1 and check(pathlist,currentcell-1)==False:
                direction.append(currentcell - 1)
    if check(fblacknum,currentcell+8)==False and int((currentcell)+8) <= 64 and check(pathlist,currentcell+8)==False:
                direction.append(currentcell + 8)
    if check(fblacknum,currentcell-8)==False and int((currentcell)-8) >= 1  and check(pathlist,currentcell-8)==False:
                direction.append(currentcell - 8)
    if len(direction) > 0:
        c = random.choice(direction)
        pathlist.append(c)
        fpathlist.append(c)
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
        if len(randomlist)>0:
            choice=random.choice(randomlist)
            fblacknum.remove(choice)
        if len(randomlist)==0:
            fpathlist.remove(currentcell)
            d=check(blacknum,currentcell)
            if d==True:
                fblacknum.append(currentcell)
            currentcell=fpathlist[(len(fpathlist))-1]

status='not reached'
num=0
currentcell=64
pathlist=[0]
actualpathlist=[64]
while status=='not reached':
    s=checkflodfill(pathlist,num)
    num=num+1
    for i in range (len(s)):
        if check(fblacknum, actualpathlist[s[i]] + 1) == False and (actualpathlist[s[i]] % 8) != 0 and check(actualpathlist,actualpathlist[s[i]] + 1) == False:
            pathlist.append(num)
            actualpathlist.append(actualpathlist[s[i]] + 1)
        if check(fblacknum, actualpathlist[s[i]] - 1) == False and (actualpathlist[s[i]] % 8) != 1 and check(actualpathlist,actualpathlist[s[i]] - 1) == False:
            pathlist.append(num)
            actualpathlist.append(actualpathlist[s[i]] - 1)
        if check(fblacknum, actualpathlist[s[i]] + 8) == False and int((actualpathlist[s[i]] + 8)) <=64 and check(actualpathlist,actualpathlist[s[i]] +8) == False:
            pathlist.append(num)
            actualpathlist.append(actualpathlist[s[i]] + 8)
        if check(fblacknum, actualpathlist[s[i]] - 8) == False and int((actualpathlist[s[i]] - 8)) >=1 and check(actualpathlist,actualpathlist[s[i]] - 8) == False:
            pathlist.append(num)
            actualpathlist.append(actualpathlist[s[i]] - 8)
    s = checkflodfill(pathlist, num)
    for i in range(len(s)):
        if actualpathlist[s[i]]==1:
            status='reached'
            break


print(fpathlist)
display(fblacknum,0,cell2)
print(fblacknum)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if number==65:
            font=pygame.font.SysFont("comicsansms", 50)
            for i in range(len(pathlist)):
                text = font.render(str(pathlist[i]), True, (0, 128, 0))
                x = (((actualpathlist[i] - 1) % 8) * 75)
                y = ((int((actualpathlist[i] - 1) / 8)) * 75)
                screen.blit(text, (x, y))
                pygame.display.update()
            number=1