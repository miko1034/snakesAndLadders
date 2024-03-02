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
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
		]

def updateVisibleGrid(grid_positions,visible_grid):
	for i in range(len(visible_grid)):
		print(visible_grid[i])
	pos = 0
	while True:
		if pos >= 100:
			print("you win")
			break
		pos = pos + int(input("enter amount to move: "))
		pastPlayerPos = [0,0]
		for i in range(len(grid_positions)):

			if pos in grid_positions[i]:
				playerPos = [i,grid_positions[i].index(pos)]
				visible_grid[playerPos[0]][playerPos[1]] = 1
				print(f"playerPos: {playerPos}\npastPlayerPos: {pastPlayerPos}")
				pastPlayerPos = playerPos
				visible_grid[pastPlayerPos[0]][pastPlayerPos[1]] = 0
				print(f"pastPlayerPos: {pastPlayerPos}")

		for i in range(len(visible_grid)):
			print(visible_grid[i])


updateVisibleGrid(grid_positions,visible_grid)