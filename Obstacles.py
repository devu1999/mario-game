import random
import sys,os
import time
class obstacles:
	def __init__(self,height, lower, upper,obj,x):
		self.col = random.randint(lower,upper)
		self.height = 2
		self.headx = x
		obj.Gamepad[x-1-self.height][self.col] = "\033[1;93m$\033[0m"
		obj.Gamepad[x-1-self.height][self.col+1] = "\033[1;93m$\033[0m"
		obj.Gamepad[x-1-self.height][self.col+2] = "\033[1;93m$\033[0m"

	def Build(self,obj):
		for i in range(self.headx-self.height,self.headx):
			obj.Gamepad[i][self.col] = "\033[41;31m#\033[0m"
			obj.Gamepad[i][self.col+1] = "\033[41;31m#\033[0m"
			obj.Gamepad[i][self.col+2] = "\033[41;31m#\033[0m"


class cloud:
	def __init__(self):
		self.x = random.randint(1,5)
		self.y = random.randint(1,70)


	def Build(self,obj):
		obj.Gamepad[self.x][self.y] = "\033[36m_\033[0m"
		obj.Gamepad[self.x][self.y+1] = "\033[36m_\033[0m"
		obj.Gamepad[self.x+1][self.y] = "\033[46;36m \033[0m"
		obj.Gamepad[self.x+1][self.y+1] = "\033[46;36m \033[0m"
		obj.Gamepad[self.x+1][self.y -1] ="\033[36m(\033[0m"
		obj.Gamepad[self.x+2][self.y - 1] ="\033[46;36m \033[0m"
		obj.Gamepad[self.x+2][self.y ] ="\033[46;36m \033[0m"
		obj.Gamepad[self.x+2][self.y +2] ="\033[47;36m \033[0m"
		obj.Gamepad[self.x+2][self.y +3] ="\033[47;36m \033[0m"
		obj.Gamepad[self.x+1][self.y + 2] ="\033[36m)\033[0m"
		obj.Gamepad[self.x+2][self.y -2] ="\033[36m(\033[0m"
		obj.Gamepad[self.x+2][self.y + 1] ="\033[36m)\033[0m"
		obj.Gamepad[self.x+2][self.y + 4] ="\033[36m)\033[0m"
		obj.Gamepad[self.x +3][self.y-1] = "\033[36m_\033[0m"
		obj.Gamepad[self.x +3][self.y] = "\033[36m_\033[0m"
		obj.Gamepad[self.x +3][self.y +2] = "\033[36m_\033[0m"
		obj.Gamepad[self.x +3][self.y + 3] = "\033[36m_\033[0m"

class flag:
	def __init__(self):
		pass

	def Build(self,obj,x,y):
		obj.Gamepad[x][y] = "E"
		obj.Gamepad[x][y+1] = "N"
		obj.Gamepad[x][y+2] = "D"
		for i in range(x+2,20):
			obj.Gamepad[i][y+2] = "|"
		obj.Gamepad[x+2][y] = "/"
		obj.Gamepad[x+3][y] = "|"
		obj.Gamepad[x+4][y] = "\\"
		obj.Gamepad[x+1][y+1] = "_"
		obj.Gamepad[x+4][y+1] = "_"

	def clear(self,obj,x,y):
		obj.Gamepad[x][y] = " "
		obj.Gamepad[x][y+1] = " "
		obj.Gamepad[x][y+2] = " "
		for i in range(x+2,20):
			obj.Gamepad[i][y+2] = " "
		obj.Gamepad[x+2][y] = " "
		obj.Gamepad[x+3][y] = " "
		obj.Gamepad[x+4][y] = " "
		obj.Gamepad[x+1][y+1] = " "
		obj.Gamepad[x+4][y+1] = " "

	def animation(self,Gameboard):
		start_time = time.time()
		x = 10
		while(x <= 16):
			pass
			y = 78
			self.clear(Gameboard,x,y)
			self.Build(Gameboard,x,y)
			if(time.time() - start.time() >= (x-9)*0.2):
				x += 1