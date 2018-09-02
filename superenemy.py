from bullet import *
import sys,os
class superenemy():
    def __init__(self,x,y):
        self.headx = 15
        self.heady = y
        self.direction = 'R'

    def  Build(self,obj,Mario):
        char = ["0","|","/","\\"]
        for i in range(0,len(char)):
            char[i] = "\033[37m" + str(char[i]) + "\033[0m"
            for j in range(self.headx+2,self.headx + 5):
                if(obj.Gamepad[j][self.heady - 3] == char[i]):
                    Mario.clearplayer(obj.Gamepad)
                    return -1;
        for i in range(15,20):
            obj.Gamepad[i][self.heady] = "\033[41;31m#\033[0m"
        for i in range(self.heady-2,self.heady+3):
                        obj.Gamepad[17][i] = "\033[41;31m#\033[0m"
                        obj.Gamepad[18][i] = "\033[41;31m#\033[0m"
        list = [15,17,19]
        for i in range(0,len(list)):
            for j in range(self.heady-1,self.heady +2):
                obj.Gamepad[list[i]][j] = "\033[41;31m#\033[0m"


        obj.Gamepad[16][self.heady-2] = "\033[41;31m#\033[0m"
        obj.Gamepad[16][self.heady] = "\033[41;31m#\033[0m"
        obj.Gamepad[16][self.heady+2] = "\033[41;31m#\033[0m"
        return 1;


    def  clear(self,obj):
        for i in range(15,20):
            obj.Gamepad[i][self.heady] = " "
        for i in range(self.heady-2,self.heady+3):
                        obj.Gamepad[17][i] = " "
                        obj.Gamepad[18][i] = " "
        list = [15,17,19]
        for i in range(0,len(list)):
            for j in range(self.heady-1,self.heady +2):
                obj.Gamepad[list[i]][j] = " "


        obj.Gamepad[16][self.heady-2] = " "
        obj.Gamepad[16][self.heady] = " "
        obj.Gamepad[16][self.heady+2] = " "

    def updatepos(self,obj):
        if(self.direction == "R"):
            if(obj.Gamepad[self.headx + 3][self.heady + 3] != "\033[41;31m#\033[0m" and self.heady <= 70):
                self.heady += 1
            else:
                self.direction = "L"
            if(obj.Gamepad[self.headx + 1][self.heady + 3] == "*"):
                return -1

        else:
            if(obj.Gamepad[self.headx + 3][self.heady - 3] != "\033[41;31m#\033[0m" and self.heady >=1):
                self.heady -= 1
            else:
                self.direction = "R"
            if(obj.Gamepad[self.headx + 1][self.heady - 3] == "*"):
                return -1
        return 0

class superbullet(bullet):


    def firebullet(self,obj,enlist):
        list = [14,17]
        for i in list: 
            obj.Gamepad[i][self.heady] = " " 
            if(obj.Gamepad[i][self.heady- 1] == "#" or self.heady <= 3):
                return -1;
            elif(obj.Gamepad[i][self.heady - 1] == " "):
                self.heady -= 1 
            else:
                chararr = ["0","|","/","\\"]
                for i in range(0,len(self.chararr)):
                    if(obj.Gamepad[i][self.heady - 1] == chararr[i]):
                        return -1
            obj.Gamepad[i][self.heady] = "*"
        return 1




        



