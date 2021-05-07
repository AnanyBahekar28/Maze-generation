import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("8x8 Arena")

# initial bot coordinates
init_x = 17
init_y = 17

# blank map for generation
map_og = [[2,"","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",""],
          ["","","","","","","",3]]

# Importing the required images
bot_img_temp = pygame.image.load("C://Users/pallu/Desktop/Python_Anany/8x8 Arena/Bot Icon.png")
empty = pygame.image.load("C://Users/pallu/Desktop/Python_Anany/8x8 Arena/0.png")
closed = pygame.image.load("C://Users/pallu/Desktop/Python_Anany/8x8 Arena/1.png")
start_pos = pygame.image.load("C://Users/pallu/Desktop/Python_Anany/8x8 Arena/2.png")
target = pygame.image.load("C://Users/pallu/Desktop/Python_Anany/8x8 Arena/3.png")
pixel = pygame.image.load("C://Users/pallu/Desktop/Python_Anany/8x8 Arena/1-dot.png")


# Transforming images as required
bot_img = pygame.transform.scale(bot_img_temp, (70, 70))


# global variables
event = ""
x = 0
y = 0
elements_for_random = ["left","right","up","down"]

# image config
map_elements = {
    0: empty,
    2: start_pos,
    1: closed,
    3: target,
    "": closed
}

#%%

# creating maze on python
def createPygame(maze):
    # Co-ordinates for displaying the images in specific cells.
    createX = 0
    createY = 0

    for a in maze:
        createY = 0

        for b in a:
            screen.blit(map_elements[b], (createY, createX))
            createY += 100
        createX += 100

#%%

# main functions

class createMaze:
    def __init__(self, list , x, y, map_class):
        self.list = list
        self.x = x
        self.y = y
        self.map_class = map_class

    def createCells():
        screen.blit(map_elements[2],(0,0))
        screen.blit(map_elements[3],(700,700))

    def available_dirs(list,x,y):
        new_list = list
        if y == 7 and "down" in new_list:
            new_list.remove("down")
        if x == 0 and "left" in new_list:
            new_list.remove("left")
        if y == 0 and "up" in new_list:
            new_list.remove("up")
        if x == 7 and "right" in new_list:
            new_list.remove("right")
        # print(new_list)
        return new_list
    
    def createMaze(map_class, x, y, main_list):
        change_map = map_class
        if x != 7:
            if change_map[y][x+1] == 1 and "right" in main_list:
                main_list.remove("right")
        if x != 0:
            if change_map[y][x-1] == 1 and "left" in main_list:
                main_list.remove("left")
        if y != 7:
            if change_map[y+1][x] == 1 and "down" in main_list:
                main_list.remove("down")
        if y != 0:
            if change_map[y-1][x] == 1 and "up" in main_list:
                main_list.remove("up")
        while x != 7 and y != 7:
            change_map = map_class
            path_towards = random.choice(main_list)
            if path_towards == "right":
                x += 1
            elif path_towards == "left":
                x -= 1
            elif path_towards == "up":
                y -= 1
            elif path_towards == "down":
                y += 1
            if x == 7 or y == 7:
                break
            change_map[y][x] = 1
        return change_map

#%%

createMaze.createCells()
# main_list = createMaze.available_dirs(elements_for_random, x, y)
# mapFinal = createMaze.createMaze(map_og, x, y, main_list)

elements_for_random = ["left","right","up","down"]
main_list = createMaze.available_dirs(elements_for_random, x, y)
mapFinal = createMaze.createMaze(map_og, x, y, main_list)

elements_for_random = ["left","right","up","down"]
main_list = elements_for_random

while True:
    pygame.display.update()
    
    elements_for_random = ["left","right","up","down"]
    main_list_ran = elements_for_random
    print("Hi    List:", main_list_ran)

    main_list = createMaze.available_dirs(main_list_ran, x, y)
    mapFinal = createMaze.createMaze(map_og, x, y, main_list)
    print("Map: ",mapFinal)
    createPygame(mapFinal)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event = "quit"
            pygame.quit()
            break
    if event == "quit":
        break

#%%

# createMaze.createCells()
# lists = createMaze.available_dirs(elements_for_random, x, y)
# print(lists)

# def createMaze():
# 	global event, map_elements

# 	def createPath():
# 		screen.blit(map_elements[2],(0,0))
# 		screen.blit(map_elements[3],(700,700))

# 		def path_left(x):
# 			if x > 0:
# 				x -= 1
# 			else:
# 				x = 0
# 		def path_right(x):
# 			if x < 7:
# 				x += 1
# 			else:
# 				x = 7
# 		def path_up(y):
# 			if y > 0:
# 				y -= 1
# 			else:
# 				y = 0
# 		def path_down(y):
# 			if y < 7:
# 				y += 1
# 			else:
# 				y = 7
		
# 		# dictionary for functions
# 		function_dict = {"left": path_left(x), "right": path_right(x), "up": path_up(y), "down": path_down(y)}
# 		elements_for_random = ["left","right","up","down"]
# 		path_towards = random.random(elements_for_random)
# 		function_dict[path_towards]