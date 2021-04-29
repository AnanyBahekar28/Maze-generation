"""
Set the start cell
Set the target cell
mapFound = False
def RecreateMap():
    Generate the arena with random open and close blocks
Loop until mapFound == True
    Check the cells around the bot using the '8x8 Arena' code.
    Add that cell co-ordinate to the map_cells dictionary with the value 1 if that cell is open or 0 if closed. (This will be done for all the possible cells that the bot can reach)
    If current_cell in map_cells:
        reroute to other cell if open
    Else:
        Go back
    If Cell co-ordinates and blocked/closed data for all the cells == True:
        If there are blocks adjacent to the blocks tracing from the start to target cell:
            mapFound = True
            Random Workable Map Generated!
            break
    Else:
        There is no path available for the bot to travel
        RecreateMap()
"""
