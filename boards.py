import sys,os
import time
from bullet import *
from threading import Timer
import math
from inputchar import getch


rows=22
cols=81
bullets = []

class Game_Board:
	def __init__(self,rows,cols):
		self.Nrows = rows
		self.Ncols = cols
		self.Gamepad = [[' '] * cols for y in range(rows)]
		for i in range(0,cols):
			self.Gamepad[0][i] = '\033[33m_\033[0m'
			self.Gamepad[20][i] ='\033[33m_\033[0m'
		self.Time = time.time()
		self.ttime = 0
		self.no_of_coins = 0
		self.killenemy = -1

	def Windows(self):
		for row in range(2,rows-3):
			for col in range(0,cols):
				self.Gamepad[row][col]=" "


	def UpdatePosition(self,Mario,no_of_frames,enlist,bullets):
		self.killenemy = -1
		Key = getch()
		self.no_of_coins = 0
		self.no_of_coins += Mario.createPlayer(self);
		def down():
				Mario.clearplayer(self.Gamepad);
				self.killenemy = Mario.updateposition(2,0,self.Gamepad);
				self.no_of_coins += Mario.createPlayer(self);
		if Key != None:
			Mario.clearplayer(self.Gamepad);

			Key_pressed = ord(Key)
			if Key_pressed == ord('d'):
				if no_of_frames < 4:
					if Mario.heady <= 75:
						if self.Gamepad[Mario.headx + 2][Mario.heady+2] != "\033[41;31m#\033[0m": 
							self.killenemy = Mario.updateposition(0,1,self.Gamepad);
						down();
						self.no_of_coins += Mario.createPlayer(self)
					else:
						return (-1,self.no_of_coins)
				else:
					if Mario.heady <= 70:
						if self.Gamepad[Mario.headx + 2][Mario.heady+2] != "\033[41;31m#\033[0m": 
							self.killenemy = Mario.updateposition(0,1,self.Gamepad);
						down();
						self.no_of_coins += Mario.createPlayer(self)
					else:
						return (2,self.no_of_coins)

			elif Key_pressed == ord('a'):
				if Mario.heady >= 5 and self.Gamepad[Mario.headx + 2][Mario.heady-2] != "\033[41;31m#\033[0m": 
					self.killenemy = Mario.updateposition(0,-1,self.Gamepad);
					down();
				self.no_of_coins += Mario.createPlayer(self)
			elif Key_pressed == ord('w'):
				os.system('aplay jump.wav&')
				if Mario.headx >= 10 and self.Gamepad[Mario.headx - 1][Mario.heady] == " ":
					self.Time = time.time()
					Mario.clearplayer(self.Gamepad);
					self.killenemy = Mario.updateposition(-2,0,self.Gamepad);
					self.no_of_coins += Mario.createPlayer(self);
					settimer = Timer(0.3,down);
					settimer.start()
				self.no_of_coins += Mario.createPlayer(self);

			elif Key_pressed == ord('s'):
				bullets.append(bullet(Mario.headx+1,Mario.heady+2,self))
	

			elif Key_pressed == ord('q'):
				return (-5,self.no_of_coins,self.killenemy)

		return (0,self.no_of_coins,self.killenemy)


