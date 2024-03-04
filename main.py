import random
import os

#counter
class Counter:
	def __init__(self,colour,pos):
		self.colour = colour
		self.pos = pos
	def setPos(self,start,end):
		self.start = start
		self.end = end
	def getPos(self):
		return[self.start,self.end] 

#snake
class Snake:
	def __init__(self, start=0,end=0):
		self.start = start
		self.end = end
	def setPos(self,start,end):
		self.start = start
		self.end = end
	def getPos(self):
		return[self.start,self.end] 

#ladder
class Ladder:
	def __init__(self, start=0,end=0):
		self.start = start
		self.end = end

#main game
class Game:
	def __init__(self,grid="",grid_positions=""):
		self.grid = [
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
		self.grid_positions = [
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

	def rollDice(self):
		return random.randint(1,6)
	
	def genMovables(self):
		ladderCount = random.randint(1,5)
		snakeCount = random.randint(1,5)
		snakes = [Snake() for i in range(snakeCount)]
		ladders = [Ladder() for i in range(ladderCount)]
		#generates sake start and end positions
		for i in range(len(snakes)):
			snakes[i].setPos(random.randint(1,100),random.randint(1,100))
			print(snakes[i].getPos())
		#add updating the visible grid
		return snakes,ladders


	def moveCounter(self):
		#could also just check for movables in this function
		pass

	#def checkForMovables(self):
	#	pass

	def displayGrid(self):
		for i in range(len(self.grid)):
			print(self.grid[i])

	def run(self):
		while True:
			os.system("clear")
			print("----------Snakes and Ladders----------\n\n")
			print(f"Here is the current board:\n{self.displayGrid()}")
			action = int(input("Actions:\n1) Move\n2)Quit\nYour action? "))
			if action == 1:
				pass
			elif action == 2:
				pass
			else:
				print("Invalid option. Please enter again")


game = Game()
print(game.genMovables())
game.run()