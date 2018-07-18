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
facingRight = True

images = {
		
}

imagenames = [
	("idle", 1),
	("run", 11)
]

for fold in imagenames:
	images[fold[0]] = []
	for file in range(1, fold[1] + 1):
		images[fold[0]].append(pg.image.load('Images/StickFigure/Animations/' + fold[0] + '_' + ("%02d" % file) + '.png'))	

calcCol = {}
def processCollision():
	global canMoveLR, x, y, calcCol
	calcCol = map.playerDistanceInAllDirections()
	#print(calcCol)
	return

def processSpeed():
	global x, y, xm, ym, jumpCount, facingRight, anim

	def incrs(a, b):
		return a + (b if a >= 0 else -b)

	if ((calcCol["E"] - xm) > 1 if xm > 0 else (calcCol["W"] + xm) > 1):
		x += xm
		if (xm != 0):
			facingRight = (xm > 0)
			if (anim["name"] != "run"):
				anim = {
					"name": "run",
					"frame": 0
				}
		else:
			if (anim["name"] != "idle"):
				anim = {
					"name": "idle",
					"frame": 0
				}

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
anim = {
	"name": "idle",
	"frame": 0
}
def update(pg, win, ww, wh):
	processCollision()
	processInput(pg, win, ww, wh)
	processSpeed()
	global x, y, size, drawnPosOnScreen, images, facingRight

	pos = getPlayerPosOnScreen(ww, True)
	ps = (pos[2], pos[3])

	#print((len(images[anim["name"]]), round(anim["frame"])))

	cimg = images[anim["name"]][round(anim["frame"])]
	cimgscalingd = 1 * (cimg.get_width() if cimg.get_width() >  cimg.get_height() else cimg.get_height())
	cimg = pg.transform.scale(cimg, (int(pos[3] * (cimg.get_width() / cimgscalingd)), int(pos[3] * (cimg.get_height() / cimgscalingd))))
	cimg = pg.transform.flip(cimg, not facingRight, False)
	#cimg.fill([0, 0, 0])
	win.blit(
		cimg,
		( int((ww / 2) - (ps[1] / 2)), int(map.worldYToScreen(y)), ps[0], ps[1] )
	)

	anim["frame"] += 0.5
	if anim["frame"] >= len(images[anim["name"]]) - 1:
		anim["frame"] = 0
	
	# Debug Collision Box
	#pg.draw.rect(win, [0, 0, 255], getPlayerPosOnScreen(ww), 1)

	return

def getImage(row, col):
	global images
	return images[(col * 11) + row]

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