import math
from boards import *
from characters import *
import sys,os
import inputchar
from Obstacles import *
from enemy import *
import random,math
import time
from intersection import *
from superenemy import *

rows=21
cols=81
Mario = Player(17,4)
superenemy_lives = 5
superenemy_kill = 0
os.system('aplay stage_clear.wav&')

class Playzone:

    def render(self,no_of_coins,no_of_lives,enemies_killed):
        os.system('clear')
        print("Total coins :" + str(no_of_coins),end="                            ")
        print("Lives left :" + str(no_of_lives),end="                           ")
        print("Enemies killed:" + str(enemies_killed))
        print("Score:" + str(50* enemies_killed + 10* no_of_coins + 100 * superenemy_kill))
        for row in range(rows):
            for col in range(cols):
                print(Gameboard.Gamepad[row][col],end=" ")
            print("\n")
        if(no_of_frames == 4 and superenemy_lives > 0):   
            print("Live of the enemy:",end="")
            for i in range(0,superenemy_lives):
                print("\033[41;31m^\033[0m",end="")
        print("\n")
    def createObstacles(self):
        obstacle1 = obstacles(random.randint(2,3), 20, 27,Gameboard,20)
        obstacle2 = obstacles(random.randint(2,3), 27, 54,Gameboard,20)
        obstacle1.Build(Gameboard)
        obstacle2.Build(Gameboard)

    def createObstacle(self):
        obstacle1 = obstacles(random.randint(2,3), 50, 54,Gameboard,13)
        obstacle2 = obstacles(random.randint(2,3), 50, 54,Gameboard,13)
        obstacle1.Build(Gameboard)
        obstacle1.Build(Gameboard)

    def final_screen(self,no_of_coins,no_of_lives,enemies_killed,msg):
        os.system('clear')
        print("\033[1;31m")
        lines = os.get_terminal_size().lines
        for i in range(0,math.ceil(lines/2) -2):
            print()
        print(str(msg).center(os.get_terminal_size().columns))
        print(str("Total coins :" + str(no_of_coins)).center(os.get_terminal_size().columns))
        print(str("Enemies killed:" + str(enemies_killed)).center(os.get_terminal_size().columns))
        print(str("Score:" + str(50* enemies_killed + 10* no_of_coins + 100 * superenemy_kill)).center(os.get_terminal_size().columns))
        for i in range(0,math.ceil(lines/2) -2):
            print()
        print("\033[0m")

retvalue = -1
player_alive = 0
killenemy = -1

no_of_lives = 3
no_of_frames = 0
start_time_of_enemy = time.time()
no_of_coins = 0
enemies_killed = 0
enlist = []
bullets = []


while True:
    if(retvalue == -1 and no_of_frames < 4):
        os.system('aplay world_clear.wav&')
        time.sleep(0.01)
        no_of_frames += 1
        cloudarr = []
        enlist = []
        Mario = Player(17,4)
        Gameboard = Game_Board(rows,cols)
        Begin = Playzone()
        Gameboard.Windows()
        for i in range(0,int(no_of_frames)):
            enlist.append(i)
            enlist[i] = enemy(Gameboard)
        if(no_of_frames == 4):
            Flag = flag()
            Senemy = superenemy(5,random.randint(40,70))
            Senemy.Build(Gameboard,Mario)
            Flag.Build(Gameboard,10,78)        

        Begin.createObstacles()
        Begin.createObstacles()
        no_of_cloud = random.randint(0,10) + 5;
        for i in range(0,no_of_cloud):
            cloudarr.append('c' + str(i))
            cloudarr[i] = cloud()
        no_of_coins += Mario.createPlayer(Gameboard)
        
    elif(retvalue == 2):
        Mario.clearplayer(Gameboard.Gamepad)
        Begin.final_screen(no_of_coins,no_of_lives,enemies_killed,"YOU WON!!!!!!")
        exit()
    if(no_of_lives == 0):
        Mario.clearplayer(Gameboard.Gamepad)
        Begin.final_screen(no_of_coins,no_of_lives,enemies_killed,"YOU LOST!!!!!!")
        exit()

    if(no_of_frames == 4):
        if(Mario.heady >= 70 ):
            Mario.clearplayer(Gameboard.Gamepad)
            os.system('aplay flagpole.wav&')
           #     Flag.animation(Gameboard)
            Begin.final_screen(no_of_coins,no_of_lives,enemies_killed,"YOU WON!!!!!!")
            exit()
    #enemy launching
    if(time.time() - start_time_of_enemy >= 0.05):
        temp = []
        if(no_of_frames >=4):
            Senemy.clear(Gameboard)
            superenemy_lives+=Senemy.updatepos(Gameboard)
            if(superenemy_lives == 0):
                superenemy_kill = 1
        for i in range(0,len(enlist)):
            enlist[i].clearenemy(Gameboard)
            enemy_alive = enlist[i].updatepos(Gameboard)
            collision = enlist[i].collision(Mario)
            if(enemy_alive == 1 and collision == 1):
                temp.append(enlist[i])
            else:
                os.system('aplay power.wav&')
                enemies_killed += 1
        enlist = temp

    if(time.time() - start_time_of_enemy >= 0.01):
        temp = []
        for i in range(0,len(bullets)):
            retvalue = bullets[i].move(Gameboard,enlist)
            if(retvalue == 1):
                temp.append(bullets[i])
        bullets= temp
        start_time_of_enemy = time.time()

    for i in range(0,no_of_cloud):
        cloudarr[i].Build(Gameboard)  
    if(superenemy_lives > 0 and no_of_frames >= 4):
        player_alive = Senemy.Build(Gameboard,Mario )
    for i in range(0,len(enlist)):
        player_alive = enlist[i].Build(Gameboard,Mario)
        if(player_alive == -1):
            os.system('aplay death.wav&')
            Mario.clearplayer(Gameboard.Gamepad)
            Mario.headx = 17
            Mario.heady = 4
            break
    if(player_alive == -1):
        os.system('aplay death.wav&')
        Mario.clearplayer(Gameboard.Gamepad)
        Mario = Player(17,4)
        no_of_lives -= 1


    retarr = Gameboard.UpdatePosition(Mario,no_of_frames,enlist,bullets)
    retvalue = retarr[0]
    if(retvalue == -5):
        Begin.final_screen(no_of_coins,no_of_lives,enemies_killed,"UNEXPECTED EXIT!!!!!!")
        exit()
    no_of_coins += retarr[1]




    Begin.render(no_of_coins,no_of_lives,enemies_killed)

