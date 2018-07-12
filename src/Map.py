# Map.py

from Math import Collision as collis
import Player as player

from Maps import MENU
from Maps import LEVEL1
from Maps import LEVEL2

cm = "MENU"
mapObjects = globals()[cm].data

def setMap(map):
	global cm, mapObjects
	player.x, player.y = 50, 50
	cm = map
	mapObjects = globals()[cm].data
	return

def getMap():
	return cm

# DESC: Calculates Were An Object Can Move Without Colliding Into Walls
# @params x1, y1, x2, y2 The Objects Direction (0% - 100% for All) 
# @param How much you want to move in any peticular direction (0% - 100%)
# RETURN: 4 Long Boolean Array in which it can move [north, east, south, west]
def CalculateCollision(x1, y1, x2, y2, movement):
	r = [True, True, True, True]
	for i in mapObjects:
		# Only Calculate Collision For Specified Collision Objects
		try:
			if i.lineCollision:
				# North
				if collis.rectOverlapLine([x1, y1 - movement, x2, y2 - movement], [i.x1 * 100, i.y1 * 100, i.x2 * 100, i.y2 * 100]):
					r[0] = False
				# East
				if collis.rectOverlapLine([x1 + movement, y1, x2 + movement, y2], [i.x1 * 100, i.y1 * 100, i.x2 * 100, i.y2 * 100]):
					r[1] = False
				# South
				if collis.rectOverlapLine([x1, y1 + movement, x2, y2 + movement], [i.x1 * 100, i.y1 * 100, i.x2 * 100, i.y2 * 100]):
					r[2] = False
				# West
				if collis.rectOverlapLine([x1 - movement, y1, x2 - movement, y2], [i.x1 * 100, i.y1 * 100, i.x2 * 100, i.y2 * 100]):
					r[3] = False
		except AttributeError:
			pass
	return r

def updateMap():
	globals()[cm].update()