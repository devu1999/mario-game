import sys,os
class bullet:
    def __init__(self,x,y,obj):
        self.x = x
        self.y = y
        obj.Gamepad[x][y] = "*"

    def move(self,obj,enlist):
        obj.Gamepad[self.x][self.y] = " " 
        if(obj.Gamepad[self.x][self.y+1] == "\033[41;31m#\033[0m"  or self.y >= 75):
            return -1;
        elif(obj.Gamepad[self.x][self.y + 1] == " "):
            self.y += 1 
        else:
            for i in range(0,len(enlist)):
                if(self.y == enlist[i].y):
                    enlist.remove(enlist[i])
                    break
            return -1
        obj.Gamepad[self.x][self.y] = "*"
        return 1

