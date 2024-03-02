import random

#counter
class Counter:
	def __init__(self,colour,pos):
		self.colour = colour
		self.pos = pos
	def changePos(self,usrinp):
		self.pos = usrinp
		return 

#snake
class Snake:
	def __init__(self, start=0,end=0):
		self.start = start
		self.end = end

#ladder
class Ladder:
	def __init__(self, start=0,end=0):
		self.start = start
		self.end = end

#main game
class Game:
	def __init__(self,grid=""):
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


	def rollDice(self):
		pass

	def moveCounter(self):
		pass

	def checkForMovables(self):
		pass

	def run(self):
		print(f"Here is your grid: {self.grid}")



game = Game()
game.run()