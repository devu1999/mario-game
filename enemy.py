import random
import sys,os
class enemy():
    def __init__(self,obj):
        self.x = 18
        self.y = random.randint(10,75)
        self.direction = 'R'
        self.char = []
        while( obj.Gamepad[self.x][self.y] != " " and obj.Gamepad[self.x + 1][self.y] != " "):
            self.y = random.randint(0,75)

    def Build(self,obj,Mario):
        self.char = ["0","|","/","\\"]
        for i in range(0,len(self.char)):
            self.char[i] = "\033[37m" + str(self.char[i]) + "\033[0m"
            if(obj.Gamepad[self.x][self.y] == self.char[i]):
                Mario.clearplayer(obj.Gamepad)
                return -1;
        obj.Gamepad[self.x][self.y] = "^"
        obj.Gamepad[self.x + 1][self.y] = "T"
        return 1

    def clearenemy(self,obj):
        obj.Gamepad[self.x][self.y] = " "
        obj.Gamepad[self.x + 1][self.y] = " "

    def updatepos(self,obj):
        if(self.direction == "R"):
            if(obj.Gamepad[self.x][self.y + 1] != "\033[41;31m#\033[0m" and self.y <= 77):
                self.y += 1
            else:
                self.direction = "L"
            if(obj.Gamepad[self.x][self.y + 1] == "*"):
                return -1

        else:
            if(obj.Gamepad[self.x][self.y - 1] != "\033[41;31m#\033[0m" and self.y >=1):
                self.y -= 1
            else:
                self.direction = "R"
            if(obj.Gamepad[self.x][self.y - 1] == "*"):
                return -1
        return 1

    def collision(self,Mario):
        if(Mario.headx - self.x < -1 and self.y >= Mario.heady - 1 and self.y <= Mario.heady + 1):
            return -1;
        return 1;






















































































































































































































































































































