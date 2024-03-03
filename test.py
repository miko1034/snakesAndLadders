#import random
#import time

grid_positions = [
	[100,99,98,97,96,95,94,93,92,91],
	[81,82,83,84,85,86,87,88,89,90],
	[80,79,78,77,76,75,74,73,72,71],
	[61,62,63,64,65,66,67,68,69,70],
	[60,59,58,57,56,55,54,53,52,51],
	[41,42,43,44,45,46,47,48,49,50],
	[40,39,38,37,36,35,34,33,32,31],
	[21,22,23,24,25,26,27,28,29,30],
	[20,19,18,17,16,15,14,13,12,11],
	[1,2,3,4,5,6,7,8,9,10],
		]

visible_grid = [
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0], # make function that clears all player positions from grid
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
		]

def updateVisibleGrid(grid_positions,visible_grid):
	#prints visible grid
	for i in range(len(visible_grid)):
		print(visible_grid[i])
	#tries to find index of player position and update the visible grid of the same index to a 1
	playerPos = 1 #<-- start of the board
	while True:
		playerPos += int(input("enter the amount to move: "))
		for i in range(len(grid_positions)): # cycles through the 
			if playerPos in grid_positions[i]:
				currentPos = [i,grid_positions[i].index(playerPos)]
				visible_grid[currentPos[0]][currentPos[1]] = 1
				pastPos = currentPos
				currentPos
				




updateVisibleGrid(grid_positions,visible_grid)