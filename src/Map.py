# Map.py

from Math import Collision as collis
import Player as player
import Main as main
import pygame as pg



# Maps
from Maps import MENU
from Maps import LEVEL1
from Maps import LEVEL2
from Maps import LEVEL3



# Map Stuff
cm = "MENU"
#cm = "LEVEL2"
mapObjects = globals()[cm].data

def setMap(map):
	global cm, mapObjects
	player.x, player.y = 0, 500
	player.inUi = False
	cm = map
	mapObjects = globals()[cm].data
	return

def getMap():
	return cm

def updateMap():
	globals()[cm].update()

width, height, win = 0, 0, None
def docWH(w, h, window):
	global width, height, win
	width, height = w, h
	win = window

# Physics
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
					# Filter Through Directions
					for i in dir:
						if (dst < r[i]):
							r[i] = dst

		except AttributeError:
			pass

	return r

# Cordinates
def worldXToScreen(x):
	global width, height
	return (width if width < height else height) * ((x - player.x) / 1000) + player.getPlayerPosOnScreen(width)[0]

def worldYToScreen(y):
	global width, height
	return (width if width < height else height) * ((-y + (height / 1.1)) / 1000)

def worldCordToScreen(cord):
	global width, height
	return [worldXToScreen(cord[0]), worldYToScreen(cord[1])]

def worldUnitToScreen(unit):
	global width, height
	return (width if width < height else height) * (unit / 1000)

#def screenXToWorld(x):
#	global width, height
#	return (((x / (width if width < height else height)) - player.getPlayerPosOnScreen(width)[0]) * 1000) + player.x
#
#def screenYToWorld(y):
#	global width, height
#	return (((y / (width if width < height else height)) * 1000) - (height / 1.1)) * -1
#
#def screenCordToWorld(cord):
#	global width, height
#	return [screenXToWorld(cord[0]), screenYToWorld(cord[1])]


# Debugging
def DebugPoint(p1, color=[0, 255, 0], width=5, WC=True):
	global win
	if win != None:
		if WC:
			x = int(worldXToScreen(p1[0]))
			y = int(worldYToScreen(p1[1]))
		else:
			x = int(p1[0])
			y = int(p1[1])

		pg.draw.circle(win, color, (x, y), width, 0)
	return

def DebugLine(p1, p2, color=[255, 0, 0], thicc=1):
	global win
	if win != None:
		pg.draw.line(win, color, (int(worldXToScreen(p1[0])), int(worldYToScreen(p1[1]))), (int(worldXToScreen(p2[0])), int(worldYToScreen(p2[1]))), thicc)
	return

def DebugRect(r1, color=[0, 0, 255], width=2):
	global win
	if win != None:
		pg.draw.rect(win, color, (
			int(worldXToScreen(r1[0])), 
			int(worldYToScreen(r1[1])), 
			int(worldXToScreen(r1[2]) - worldXToScreen(r1[0])), 
			int(worldYToScreen(r1[3]) - worldYToScreen(r1[1]))
		), width)
	return

def DebugText(text, p1, s=10, color=[0, 0, 0]):
	global win
	TextSurf = pg.font.Font('Fonts/Roboto-Regular.ttf', int(s)).render(str(text), True, color)
	TextRect = TextSurf.get_rect()
	TextRect.center = [worldXToScreen(p1[0]), worldYToScreen(p1[1])]
	win.blit(TextSurf, TextRect)