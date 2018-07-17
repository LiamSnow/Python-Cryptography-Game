import Map as map
import pygame as pg
import time

# Player.py

# In Percent (no decimal)
x, y = 0, 0
xm, ym = 0, 0
size = (30, 120)
movementSpeed = 1
jumpCount = 0

image = pg.image.load('Images/StickFigure.png')

calcCol = {}
def processCollision():
	global canMoveLR, x, y, calcCol
	calcCol = map.playerDistanceInAllDirections()
	#print(calcCol)
	return

def processSpeed():
	global x, y, xm, ym, jumpCount

	def incrs(a, b):
		return a + (b if a >= 0 else -b)

	if ((calcCol["E"] - xm) > 1 if xm > 0 else (calcCol["W"] + xm) > 1):
		x += xm

	if ((calcCol["N"] - ym) > 1 if ym > 0 else (calcCol["S"] + ym) > 1):
		y += ym
	else:
		if ((calcCol["S"] + ym) <= 1):
			jumpCount = 0
		ym = 0

	if (calcCol["S"] > 0):
		ym -= 0.3

	return

def processInput(pg, win, ww, wh):
	global x, y, xm, ym, movementSpeed, jumpCount
		
	movementSpeed = 3

	def getKeyPress(key):
		return (pg.key.get_pressed()[ord(key)])


	if (getKeyPress('a') or getKeyPress('d')):
		# Left
		if (getKeyPress('a')):
			xm = -movementSpeed
	
		# Right
		if (getKeyPress('d')):
			xm = movementSpeed
	else:
		xm = 0
	
	#Jump
	if (getKeyPress('w') and jumpCount < 5):
		ym = 12
		jumpCount += 1

	return

drawnPosOnScreen = []
def update(pg, win, ww, wh):
	processCollision()
	processInput(pg, win, ww, wh)
	processSpeed()
	global x, y, image, size, drawnPosOnScreen

	pos = getPlayerPosOnScreen(ww, True)
	ps = (pos[2], pos[3])
	win.blit(pg.transform.scale(image, (pos[3], pos[3])), ( int((ww / 2) - (ps[1] / 2)), int(map.worldYToScreen(y)), ps[0], ps[1] ))

	#pg.draw.rect(win, [0, 0, 255], getPlayerPosOnScreen(ww), 1)

	return

def getPlayerPosOnScreen(ww, image=False):
	global size
	ps = (
		int(map.worldUnitToScreen(size[0])),
		int(map.worldUnitToScreen(size[1]))
	)
	return ( int((ww / 2) - (ps[0] / 2)), int(map.worldYToScreen(y)), ps[0], ps[1] )

def getCollisionBox():
	global x, y, size
	return [x, y, x + size[0], y - size[1]]