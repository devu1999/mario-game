
# class intersection:
# 	def __init__(self):
# 		pass

def checkwithenemy(obj1,Gameboard):
	if(Gameboard.Gamepad[obj1.headx+3][obj1.heady-1] == "^" or Gameboard.Gamepad[obj1.headx+3][obj1.heady] == "^" or Gameboard.Gamepad[obj1.headx+3][obj1.heady+1] == "^"):
		return 1;
	elif(Gameboard.Gamepad[obj1.headx][obj1.heady+2] == "^" or Gameboard.Gamepad[obj1.headx+1][obj1.heady+2] == "^" or Gameboard.Gamepad[obj1.headx+2][obj1.heady+2] == "^"):
		return -1;
	else:
		return 0;
