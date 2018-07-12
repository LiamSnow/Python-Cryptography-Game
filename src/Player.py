import Map as map

# Player.py

# In Percent (no decimal)
x, y = 50, 50
jump = 0

def processInput(pg, win, ww, wh):
	global ProcessMovementRecursionCount
	ProcessMovementRecursionCount = 0
	def ProcessMovement(movementSpeed):
		global x, y, ProcessMovementRecursionCount
		if (pg.key.get_pressed()[119] or pg.key.get_pressed()[115] or pg.key.get_pressed()[97] or pg.key.get_pressed()[100]):
			col = map.CalculateCollision(getCollisionBox(True, False)[0], getCollisionBox(True, False)[1], getCollisionBox(True, False)[2], getCollisionBox(True, False)[3], movementSpeed * 2)

			# Up
			if (pg.key.get_pressed()[119] and col[0]):
				y -= movementSpeed
			elif not col[0] and ProcessMovementRecursionCount < 3:
				ProcessMovementRecursionCount += 1
				ProcessMovement(movementSpeed / 2)
	
			# Down
			if (pg.key.get_pressed()[115] and col[2]):
				y += movementSpeed
			elif not col[2] and ProcessMovementRecursionCount < 3:
				ProcessMovementRecursionCount += 1
				ProcessMovement(movementSpeed / 2)

			# Left
			if (pg.key.get_pressed()[97] and col[3]):
				x -= movementSpeed
			elif not col[3] and ProcessMovementRecursionCount < 3:
				ProcessMovementRecursionCount += 1
				ProcessMovement(movementSpeed / 2)
	
			# Right
			if (pg.key.get_pressed()[100] and col[1]):
				x += movementSpeed
			elif not col[1] and ProcessMovementRecursionCount < 5:
				ProcessMovementRecursionCount += 1
				ProcessMovement(movementSpeed / 2)

	ProcessMovement(ww / 5000)

	return

def update(pg, win, ww, wh):
	processInput(pg, win, ww, wh);
	global x, y

	pg.draw.rect(win, [0, 0, 0], [x / 100 * ww, y / 100 * wh, ww * 0.1, wh * 0.1], 0)

	return

def getCollisionBox(bottomOnly=False, includeJump=False):
	xColSize = 10
	yColSize = 10
	if (bottomOnly):
		if (includeJump):
			# Bottom Jump
			return [
				x, 
				y - jump + yColSize - 0.4, 
				x + xColSize, 
				y - jump + 0.3
			]
		else:
			# Bottom
			return [
				x, 
				y + yColSize - 0.4, 
				x + xColSize, 
				y + yColSize + 0.3
			]
	elif (includeJump):
		# Jump
		return [
			x, 
			y - jump, 
			x + xColSize, 
			y - jump + yColSize
		]
	else:
		return [
			x, 
			y, 
			x + xColSize, 
			y + 10
		]

