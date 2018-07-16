# Map.py

from Math import Collision as collis
import Player as player
import Main as main

from Maps import MENU
from Maps import LEVEL1
from Maps import LEVEL2

cm = "MENU"
mapObjects = globals()[cm].data

def setMap(map):
	global cm, mapObjects
	player.x, player.y = 0, 500
	cm = map
	mapObjects = globals()[cm].data
	return

def getMap():
	return cm

""" Returns {
	"N": default 1000000,
	"E": default 1000000,
	"S": default 1000000,
	"W": default 1000000
}"""
def playerDistanceInAllDirections():
	p = player.getCollisionBox()
	r = {
		"N": 1000000,
		"E": 1000000,
		"S": 1000000,
		"W": 1000000
	}

	for i in mapObjects:
		try:
			if (i.boxPhysics):
				# Calculate Collision
				dir, dst = (collis.rectDistance(p, [(i.x1), (i.y1), (i.x2), (i.y2)]))
				
				if (dir != None and dst != None):
					#print(dir, dst)
					# Filter Through Directions
					for i in dir:
						if (dst < r[i]):
							r[i] = dst

		except AttributeError:
			pass

	return r

def updateMap():
	globals()[cm].update()

width, height = 0, 0
def docWH(w, h):
	global width, height
	width, height = w, h

def worldXToScreen(x):
	global width, height
	return (width if width < height else height) * ((x + player.x) / 1000)

def worldYToScreen(y):
	global width, height
	return (width if width < height else height) * ((-y + (height / 1.1)) / 1000)

def worldCordToScreen(cord):
	global width, height
	return [worldXToScreen(cord[0]), worldYToScreen(cord[1])]

def worldUnitToScreen(unit):
	global width, height
	return (width if width < height else height) * (unit / 1000)
