from inputchar import *
#from boards import *
from characters import *
import sys,os
from Obstacles import *
import random,math


import sys,os
class Player:
    def __init__(self,charHeadx,charHeady):
        self.headx = charHeadx
        self.heady = charHeady
        self.dummy = 0
        self.check = 0
        self.noc = 0


    def createPlayer(self,Gameboard):
        self.noc = 0
        if(Gameboard.Gamepad[self.headx][self.heady] == "\033[1;93m$\033[0m"):
            os.system('aplay coin.wav&')
            self.noc += 1
        if(Gameboard.Gamepad[self.headx+1][self.heady-1] == "\033[1;93m$\033[0m"):
            os.system('aplay coin.wav&')
            self.noc += 1
        if(Gameboard.Gamepad[self.headx+1][self.heady] == "\033[1;93m$\033[0m"):
            os.system('aplay coin.wav&')
            self.noc += 1
        if(Gameboard.Gamepad[self.headx+1][self.heady+1] == "\033[1;93m$\033[0m"):
            os.system('aplay coin.wav&')
            self.noc += 1
        if(Gameboard.Gamepad[self.headx+2][self.heady-1] == "\033[1;93m$\033[0m"):
            os.system('aplay coin.wav&')
            self.noc += 1
        if(Gameboard.Gamepad[self.headx+2][self.heady+1] == "\033[1;93m$\033[0m"):
            os.system('aplay coin.wav&')
            self.noc += 1
        Gameboard.Gamepad[self.headx][self.heady] = "\033[37m0\033[0m"
        Gameboard.Gamepad[self.headx+1][self.heady-1] = "\033[37m/\033[0m"
        Gameboard.Gamepad[self.headx+1][self.heady] = "\033[37m|\033[0m"
        Gameboard.Gamepad[self.headx+1][self.heady+1] = "\033[37m\\\033[0m"
        Gameboard.Gamepad[self.headx+2][self.heady-1] = "\033[37m/\033[0m"
        Gameboard.Gamepad[self.headx+2][self.heady+1] = "\033[37m\\\033[0m"
        return self.noc

    def updateposition(self,x_change,y_change,Gamepad):
        if(self.heady + y_change <=80 and self.heady + y_change >= 1):
                self.heady += y_change;
        if(self.headx + x_change <=20 and self.headx + x_change >= 1):
             if(x_change > 0):       
                self.dummy = self.headx + 3
                for i in  range(self.dummy,20):
                    if((Gamepad[i][self.heady -1] != "\033[41;31m#\033[0m" and Gamepad[i][self.heady] != "\033[41;31m#\033[0m" and Gamepad[i][self.heady +1] != "\033[41;31m#\033[0m")):
                        self.headx += 1
                    else:
                            break
                for i in  range(self.dummy,20):
                    if((Gamepad[i][self.heady -1] == "^" and Gamepad[i][self.heady] == "^" and Gamepad[i][self.heady +1] == "^")):
                        return 1            
             elif( x_change < 0):
                self.headx += x_change

             return -1
             
   
    def clearplayer(self,Gamepad):
        for i in range(self.headx,self.headx + 3):
            for j in range(self.heady- 1,self.heady + 2):
                if(i < 20  and i > 1  and (Gamepad[i][j] == "[37m0[0m"  or Gamepad[i][j] == "\033[37m|\033[0m" or Gamepad[i][j] == "\033[37m\\\033[0m" or Gamepad[i][j] == "\033[37m/\033[0m")):
                    Gamepad[i][j] = " ";




