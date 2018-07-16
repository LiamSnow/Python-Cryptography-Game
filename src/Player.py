import Map as map
import pygame as pg
import time

# Player.py

# In Percent (no decimal)
x, y = 0, 0
xm, ym = 0, 0
size = 120
movementSpeed = 1

image = pg.image.load('Images/StickFigure.png')

calcCol = {}
def processCollision():
	global canMoveLR, x, y, calcCol
	calcCol = map.playerDistanceInAllDirections()
	calcCol["S"] -= size
	return

def processSpeed():
	global x, y, xm, ym

	def incrs(a, b):
		return a + (b if a >= 0 else -b)

	if (xm <= calcCol[("E" if xm > 0 else "W")]):
		x += xm
	else:
		x += incrs(incrs(calcCol[("E" if xm > 0 else "W")], -3) / 10, -1)

	if (ym <= calcCol[("N" if ym > 0 else "S")]):
		y += ym

	#print(calcCol)
	if (calcCol["S"] > 0):
		ym -= 0.006

	return

def processInput(pg, win, ww, wh):
	global x, y, xm, ym, movementSpeed
		
	movementSpeed = 1

	def getKeyPress(key):
		return (pg.key.get_pressed()[ord(key)])


	if (getKeyPress('a') or getKeyPress('d')):
		# Left
		if (getKeyPress('a')):
			xm = movementSpeed
	
		# Right
		if (getKeyPress('d')):
			xm = -movementSpeed
	else:
		xm = 0

	# Jump
	if (getKeyPress('w')):
		pass

	return


def update(pg, win, ww, wh):
	processCollision()
	processInput(pg, win, ww, wh)
	processSpeed()
	global x, y, image, size

	ps = int(map.worldUnitToScreen(size))
	win.blit(pg.transform.scale(image, (ps, ps)), ( int((ww / 2) - (ps / 2)), int(map.worldYToScreen(y)) ))

	return

def getCollisionBox():
	global x, y, size
	return [x, y, x + size, y + size]