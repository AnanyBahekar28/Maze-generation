"""
 Initialize the Start,Target & Current Cell
 Initialize the Path List
 Generate 8x8 random Map with 1's & 0's
 Initialize Random_Update_List
 Loop until Path found( if Current_cell = Target_cell)
Check 1:    
    Check the cell below(y+1) the Current_cell for open or close
    If the cell is open then add that cell to Path List, 
    update the Current_cell & rerun the checks
    else Add y+1 to Random_Update_List and do the Check 2 
Check 2:
    Check the cell on the right (x+1) the Current_cell 
    If the cell is open then add that cell to Path List,
    update the Current_cell & rerun the checks
    else Add x+1 to Random_Update_List and do the Check 3
Check 3:
    Check the cell on the top(y-1) only if the cell is :
        -not in the Path List
        -not at the boundary
        
        If the cell is open then add that cell to Path List,
        update the Current_cell & rerun the check
        else Add y-1 to Random_Update_List and do the Check 4
        
Check 4:
    Check the cell on the left(x-1) only if the cell is :
        -not in the Path List
        -not at the boundary
        
        If the cell is open then add that cell to Path List,
        update the Current_cell & rerun the check
        else Add x-1 to Random_Update_List and do the Check_Failed routine
        
Check_Failed Routine:
    Generate Random numbers at the positions in the Random_Update_List
    and rerun the checks
     
"""
